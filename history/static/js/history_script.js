$(document).ready(function() {
    $(".btn-delete").click(function(event) {
        event.preventDefault(); // Mencegah submit form
        if (!confirm("Apakah Anda yakin ingin menghapus riwayat ini?")) {
            return false;
        }
        var form = $(this).closest(".form-history");
        var history_id = form.find("input[name='history_id']").val();
        
        $.ajax({
            url: 'delete/', // Ganti dengan URL endpoint untuk menghapus data
            method: 'POST',
            data: {
                'history_id': history_id,
                'csrfmiddlewaretoken': form.find("input[name='csrfmiddlewaretoken']").val()
            },
            success: function(response) {
                // Anda bisa memberikan feedback atau melakukan refresh pada elemen yang terkait.
                form.closest('.history-item').remove();
            },
            error: function(response) {
                alert('Terjadi kesalahan saat menghapus data.');
            }
        });
    });
});

$(document).ready(function() {
    $(".history-item").each(function() {
        var date = $(this).data('date');
        $(this).attr('data-group', moment(date, 'YYYYMMDD').format('YYYY-MM-DD'));
        $(this).addClass('shown');
    });

    $("#search-input").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".history-item.shown").filter(function() {
            $(this).toggle($(this).data("query").toLowerCase().indexOf(value) > -1)
        });
    });
});
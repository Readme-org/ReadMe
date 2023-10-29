$(document).ready(function() {
    $(".btn-delete").click(function() {
        if (!confirm("Apakah Anda yakin ingin menghapus riwayat ini?")) {
            return false;
        }
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
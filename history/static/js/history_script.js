$(document).ready(function() {
    $(".btn-delete").click(function() {
        if (!confirm("Apakah Anda yakin ingin menghapus riwayat ini?")) {
            return false;
        }
    });
});
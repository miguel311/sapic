$(document).ready(function() {
   $('#datatable').dataTable({
        "processing": true,
        "serverSide": true,
        "ajax": LISTAR_USER,
        language: {
            url: JSON_DATA
        }
        });
    $('#datatable')
        .removeClass('display')
        .addClass('table table-striped table-bordered');
});
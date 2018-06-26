$(document).ready(function() {
    $('#id_coordenadas_div_map').attr({
        'class':'col-md-10 col-md-offset-2 text-center'
    });
    $('.clear_features a').text('Eliminar seleccion');
    $('.clear_features a').attr({
        class: 'btn btn-warning'
    });
    $("#id_map_cartografico").fileinput({
            showCaption: true,
            previewFileType: "image",
            browseClass: "btn btn-danger",
            browseLabel: "Subir Imagen del mapa cartográfico",
            browseIcon: "<i class=\"glyphicon glyphicon-picture\"></i> ",
            removeLabel: "Eliminar",
            uploadLabel:"Actualizar",
        });   
});
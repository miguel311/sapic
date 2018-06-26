/**
 * Función para aumentar la barra de progreso si se responde la encuesta
**/
function control_progress() {
    var content = $('.carousel-inner .active');
    var not_empty = 0;
    var elements = $('.carousel-indicators li').length-1;
    $.each(content.find('input'),function(index,value){
        var name = $(value).attr('name');
        if(name.search('radio')!=-1 || name.search('check')!=-1 || name.search('sino')!=-1){
            not_empty = $(value).parent().attr('class').search('checked') !== -1 ? 1:not_empty;
            if (name.search('sino')!=-1) {
                if ($(value).parent().attr('class').search('checked') !== -1 && $(value).val()=="No") {
                    if ($(value).attr('class').search('need_justification')!=-1) {
                        var text_area = $(value).parent().parent().find('textarea');
                        not_empty = $(text_area).val().trim() !== '' ? 1:0;
                        not_empty = $(text_area).val().length >= 128 && $(text_area).val().length <= 2000  ? 1:0;
                        if ($(text_area).val().length < 128 || $(text_area).val().length >2000) {
                            bootbox.alert("La longitud de la respuesta debe estar entre 128 y 2000 cáracteres");
                        }
                    } 
                }               
            }
        }
    });
    $.each(content.find('textarea'),function(index,value){
        var name = $(value).attr('name');
        if (name.search('abierta')!==-1) {
            not_empty = $(value).val().trim() !== '' ? 1:not_empty;
            not_empty = $(value).val().length >= 128 && $(value).val().length <= 2000  ? 1:0;
            if ($(value).val().length < 128 || $(value).val().length >2000) {
                bootbox.alert("La longitud de la respuesta debe estar entre 128 y 2000 cáracteres");
            }
        }
    });
    if (not_empty) {
        $('#status .bar span').css({'color':'white'});
        $('#myCarousel').carousel('next');
        var current_value = ($('#status .progress-bar').width()/$('#status').width())*100;
        var final_value = current_value+(100/elements);
        $('#status .progress-bar').width(final_value+"%");
        
        if (final_value>=99.9) {
            $('#status .progress-bar').width("100%");
            $('#status .bar span').text("Finalizado");
            $('#status .progress-bar').addClass('progress-bar-success');
        }
    }
}

/**
 * Función para enviar los respuestas de la encuesta
 * @param event Recibe el evento
**/
function send_poll(event) {
    event.preventDefault();
    $('.btn-success').attr('disabled',true);
    var form = $("#encuesta_form");
    var routes = $(location).attr('pathname').split('/')
    var pk = routes[routes.length-3]
    var participacion;
    $.get('/validar-participacion-ajax?user='+USER+"&consulta="+ENCUESTA)
    .done(function(response){
        if (response.mensaje) {
            participacion = response.participacion
            if (participacion) {
                bootbox.alert("Este usuario Ya participó en esta encuenta <br>Será direccionado en 4 segundos");
                setTimeout(function(){
                    $(location).attr('href', $(location).attr('origin')+URL)    
                },4000);
            }
            else
            {
                $.ajax({
                    type: 'POST',
                    data: $(form).serialize(),
                    url: URL,
                    success: function(response) {
                        if (response.code == true) {
                            bootbox.alert("Se registró su participación con éxito <br>Será direccionado en 4 segundos");
                            setTimeout(function(){
                                $(location).attr('href', $(location).attr('origin')+URL)    
                            },4000);
                        }
                        else{
                            bootbox.alert("Ocurrió un error inesperado");
                            $('.btn-success').attr('disabled',false);
                        }
                    },
                        error:function(error)
                        {
                            bootbox.alert("Ocurrió un error inesperado");
                            $('.btn-success').attr('disabled',false);
                        }
                });
            }
        }
        else{
            bootbox.alert(response.error);    
        }
        })
    .fail(function(response){
        bootbox.alert("Ocurrió un error inesperado");
    });
}

/**
 * Función para retroceder en el carrusel y bajar el valor de la
 * barra de progreso
**/
function go_back() {
    var first_element = $('.carousel-indicators li')[0];
    if($(first_element).attr('class')!=='active')
    {
        $('#myCarousel').carousel('prev');
        var elements = $('.carousel-indicators li').length-1;
        var current_value = ($('#status .progress-bar').width()/$('#status').width())*100;
        var final_value = current_value-(100/elements);
        $('#status .progress-bar').width(final_value+"%");
        if (final_value!=100) {
            $('#status .bar span').text() == "Finalizado" ? $('#status .bar span').text('Progreso'):'';
            $('#status .progress-bar').removeClass('progress-bar-success');
        }
        if (final_value<=0) {
            $('#status .bar span').css({'color':'black'});
        }
    }
}
function cargar_organizciones(fk_tipo, url)
    {
        if(fk_tipo!='')
        {
            $('#organizacion_social').show("300")
            $.ajax({
                url: url,
                type: "GET",
                data: {
                    fk_tipo: fk_tipo
                },
                dataType: 'json',
                beforeSend: function(data)
                {
                    $('#id_organizacion').html('<option value="">Cargando...</option>');
                },
                success: function(data) {

                    var options = '<option value="">Seleccione Organizacion Social</option>';
                    for (var i=0; i < data.length; i++)
                    {
                        options += '<option value="'+data[i]["id"]+'">' +data[i]["nombre"] +'</option>';
                    }
                    $('#id_organizacion').html(options);
                    $("#id_organizacion option:first").attr('selected', 'selected');
                }
            });
        }
        else
        {
             $('#id_organizacion').html('<option value="">Seleccione Organizacion Social</option>');
        }
    };

function cargar_comites(fk_tipo, url)
    {
        if(fk_tipo!='' && fk_tipo==='1')
        {
            $('#comites').show("300")
            $.ajax({
                url: url,
                type: "GET",
                data: {
                    fk_unidad: fk_tipo
                },
                dataType: 'json',
                beforeSend: function(data)
                {
                    $('#id_comite_unidad_ejecutiva').html('<option value="">Cargando...</option>');
                },
                success: function(data) {
                    var options = '<option value="">Seleccione Comite del Area Ejecutiva</option>';
                    for (var i = 0; i < data.length; i++)
                    {
                        options += '<option value="'+data[i]["id"]+'">' +data[i]["tipo"] +'</option>';
                    }
                    $('#id_comite_unidad_ejecutiva').html(options);
                    $("#id_comite_unidad_ejecutiva option:first").attr('selected', 'selected');
                }
            });
        }
        else
        {
             $('#id_comite_unidad_ejecutiva').html('<option value="">Seleccione Comite del Area Ejecutiva</option>');
             $('#comites').hide("800")
        }
    };
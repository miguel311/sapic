function cargar_municipios(id_estado, url)
        {
            if(id_estado!='')
            {
                $('#municipio').show("300")
                $.ajax({
                    url: url,
                    type: "GET",
                    data: {
                        id_estado: id_estado
                    },
                    dataType: 'json',
                    beforeSend: function(data)
                    {
                        $('#id_municipio').html('<option value="">Cargando...</option>');
                        $('#id_localidad').html('<option value="">Cargando...</option>');
                    },
                    success: function(data) {
                        var options = '<option value="">Seleccione Municipio</option>';
                        for (var i = 0; i < data.length; i++)
                        {
                            options += '<option value="'+data[i]["id"]+'">' +data[i]["nombre"] +'</option>';
                        }
                        $('#id_municipio').html(options);
                        $("#id_municipio option:first").attr('selected', 'selected');
                    }
                });
            }
            else
            {
                 $('#id_municipio').html('<option value="">Seleccione Municipio</option>');
            }

            $('#id_localidad').html('<option value="">Seleccione Parroquia</option>');
        };

function cargar_parroquias(id_municipio, url)
        {
            if(id_municipio!='')
            {
                $('#parroquia').show("300")
                
                $.ajax({
                    url: url,
                    type: "GET",
                    data: {
                        id_municipio: id_municipio
                    },
                    dataType: 'json',
                    beforeSend: function(data)
                    {
                        $('#id_localidad').html('<option value="">Cargando...</option>');
                    },
                    success: function(data) {
                        var options = '<option value="">Seleccione Parroquia</option>';
                        for (var i = 0; i < data.length; i++)
                        {
                            options += '<option value="'+data[i]["id"]+'">' +data[i]["nombre"] +'</option>';
                        }
                        $('#id_localidad').html(options);
                        $("#id_localidad option:first").attr('selected', 'selected');
                    }
                });
            }
            else
            {
                 $('#id_localidad').html('<option value="">Seleccione Parroquia</option>');
            }
        }

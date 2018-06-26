# -*- coding: utf-8 -*-
"""
SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.views.genericEncuestasViews
#
# Vistas correspondientes a la explicacion situacional
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

from django.contrib import messages
from django.contrib.auth.models import (
    User
)
from django.shortcuts import render
from django.views.generic.edit import (
    FormView, UpdateView
)
from django.views.generic import (
    TemplateView, ListView
)
from django.http import JsonResponse


from explicacion_situacional.forms import (
    ExplicacionForms, UbicacionForms
    )
from explicacion_situacional.modelsEncuestas.modelsConsultas import (
    Pregunta, Consulta, Opcion
    )
from explicacion_situacional.modelsEncuestas.modelsParticipacion import (
    RespuestaSino, RespuestaOpciones,
    RespuestaAbierta, RespuestaUbicacion
    )
from explicacion_situacional.constantes import (
    TIPOS_PREGUNTAS
    )

from utils.views import LoginRequeridoPerAuth



class EncuestasParticiparView(LoginRequeridoPerAuth, TemplateView):
    """!
    Clase que gestiona la vista principal de la encuesta a la que va a participar

    @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 20-09-2017
    @version 1.0.0
    """
    template_name = "encuesta.participar.html"
    group_required = [u"Administradores", u"Voceros", u"Integrantes"]

    def get_context_data(self, **kwargs): 
        """!
        Metodo que permite cargar de nuevo valores en los datos de contexto de la vista

        @author Rodrigo Boet (rboet at cenditel.gob.ve)
        @copyright GNU/GPLv2
        @date 23-02-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param kwargs <b>{object}</b> Objeto que contiene los datos de contexto
        @return Retorna los datos de contexto
        """
        valores = {}
        try:
            consulta = Consulta.objects.select_related().get(pk=kwargs['pk'])
        except:
            consulta = ''

        for pregunta in Pregunta.objects.filter(consulta_id=kwargs['pk']).all():
            label = '<label>'+pregunta.texto_pregunta+'</label>'
            campo = ''
            if pregunta.tipo_pregunta.id == TIPOS_PREGUNTAS['SELECT_SIMPLE']:
                campo = ''
                for opcion in Opcion.objects.filter(pregunta_id=pregunta.id).all():
                    campo += '<label for="'+kwargs['pk']+'">'+opcion.texto_opcion+'</label><input type="radio" name="consulta_respuesta_radio_'+str(pregunta.id)+'" id="'+kwargs['pk']+'"value="'+str(opcion.id)+'" class="icheck">'
            elif pregunta.tipo_pregunta.id == TIPOS_PREGUNTAS['SELECT_MULTIP']:
                campo = ''
                for opcion in Opcion.objects.filter(pregunta_id=pregunta.id).all():
                    campo += '<label for="'+kwargs['pk']+'">'+opcion.texto_opcion+'</label><input type="checkbox" name="consulta_respuesta_check_'+str(pregunta.id)+'" id="'+kwargs['pk']+'"value="'+str(opcion.id)+'" class="icheck">'
            elif pregunta.tipo_pregunta.id > TIPOS_PREGUNTAS['SELECT_MULTIP'] and pregunta.tipo_pregunta.id < TIPOS_PREGUNTAS['ABIERTA']:
                campo += '<label for="'+str(pregunta.id)+'">Si</label><input type="radio" name="consulta_respuesta_sino_'+str(pregunta.id)+'" id="'+str(pregunta.id)+'"value="Si" class="icheck">'
                if(pregunta.tipo_pregunta.id == TIPOS_PREGUNTAS['SI_NO']):
                    campo += '<label for="'+str(pregunta.id)+'">No</label><input type="radio" name="consulta_respuesta_sino_'+str(pregunta.id)+'" id="'+str(pregunta.id)+'"value="No" class="icheck">'
                else:
                    campo += '<label for="'+str(pregunta.id)+'">No</label><input type="radio" name="consulta_respuesta_sino_'+str(pregunta.id)+'" id="'+str(pregunta.id)+'"value="No" class="icheck need_justification">'
                    campo += '<div id="div_justificar_'+str(pregunta.id)+'" style="display:none;"><label>Justifique su Respuesta</label>'
                    campo += '<textarea rows="20" cols="50" class="form-control" id="respuesta_justificar_'+str(pregunta.id)+'" name="consulta_respuesta_justificar_'+str(pregunta.id)+'">'
                    campo += '</textarea></div>'
            elif pregunta.tipo_pregunta.id == TIPOS_PREGUNTAS['UBICACION']:

                    campo += '<tr><th><label for="id_ubicacion'+str(pregunta.id)+'">Ubicacion:</label></th><td><style type="text/css">\
                                #id_ubicacion_map'+str(pregunta.id)+' { width: 600px; height: 400px; }\
                                #id_ubicacion_map'+str(pregunta.id)+' .aligned label { float: inherit; }\
                                #id_ubicacion_div_map'+str(pregunta.id)+' { position: relative; vertical-align: top; float: left; }\
                                #id_ubicacion'+str(pregunta.id)+' { display: none; }\
                                \
                            </style>\
                            \
                            <div id="id_ubicacion_div_map'+str(pregunta.id)+'">\
                                <div id="id_ubicacion_map'+str(pregunta.id)+'"></div>\
                                <span class="clear_features"><a href="javascript:geodjango_ubicacion.clearFeatures()">Delete all Features</a></span>\
                                \
                                <textarea id="id_ubicacion'+str(pregunta.id)+'" class="vSerializedField required" cols="150" rows="10" name="consulta_respuesta_ubicacion_'+str(pregunta.id)+'"></textarea>\
                                <script type="text/javascript">\
                                    var map_options = {};\
                                    \
                            var base_layer = new ol.layer.Tile({source: new ol.source.OSM()});\
                            \
                                    var options = {\
                                        base_layer: base_layer,\
                                        geom_name: "Unknown",\
                                        id: "id_ubicacion'+str(pregunta.id)+'",\
                                        map_id: "id_ubicacion_map'+str(pregunta.id)+'",\
                                        map_options: map_options,\
                                        map_srid: 3857,\
                                        name: "consulta_respuesta_ubicacion_'+str(pregunta.id)+'"\
                                    };\
                                    \
                            options["default_lon"] = -66;\
                            options["default_lat"] = 8;\
                            options["default_zoom"] = 5.2;\
                            \
                                    var geodjango_ubicacion = new MapWidget(options);\
                                </script>\
                            </div></td></tr>'
            else:
                campo = '<textarea rows="10" cols="50" class="form-control" name="consulta_respuesta_abierta_'+str(pregunta.id)+'"></textarea>'
            valores[pregunta.id] = {'label':label,'field':campo}
            print (valores)
            kwargs['preguntas'] = valores
            kwargs['consulta'] = consulta
        return super(EncuestasParticiparView, self).get_context_data(**kwargs)

    def post(self, request, pk):
        """!
        Metodo que sobreescribe el post del formulario

        @author Rodrigo Boet (rboet at cenditel.gob.ve)
        @copyright GNU/GPLv2
        @date 20-03-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que instancia la petición
        @param pk <b>{int}</b> Recibe el id de la consulta
        @return Retorna los datos de contexto
        """
        data = dict(request.POST)
        del data['csrfmiddlewaretoken']
        if self.request.is_ajax():
            for key in data.keys():
                parent_id = key.split("_")[-1]
                if 'sino' in key:
                    value = True if data[key][0] == 'Si' else False
                    justify_id = 'consulta_respuesta_justificar_'+str(parent_id)
                    self.crear_respuesta_sino(parent_id,value, self.request.user.id)
                    if(not value and justify_id in data.keys()):
                        respuesta = data[justify_id][0]
                        self.crear_respuesta_abierta(parent_id, respuesta,self.request.user.id,True)
                elif 'radio' in key or 'check' in key:
                    for value in data[key]:
                        self.crear_respuesta_opciones(value, self.request.user.id)
                elif 'abierta' in key:
                    value = data[key][0]
                    self.crear_respuesta_abierta(parent_id, value, self.request.user.id)
            return JsonResponse({"code":True})
        return redirect(reverse_lazy('explicacions:condicion_suelos',kwargs={'pk':pk}))

    def crear_respuesta_sino(self, parent_id, value, user_id):
        """!
        Metodo para crear una respuesta de si/no

        @author Rodrigo Boet (rboet at cenditel.gob.ve)
        @copyright GNU/GPLv2
        @date 27-03-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param parent_id <b>{int}</b> Recibe el número del id del padre
        @param value <b>{bool}</b> Recibe el valor de la respuesta
        @param user_id <b>{int}</b> Recibe el id del user
        @return Retorna los datos de contexto
        """
        user = User.objects.get(id=user_id)
        parent = Pregunta.objects.get(pk=parent_id)
        respuesta = RespuestaSino()
        respuesta.pregunta = parent
        respuesta.respuesta = value
        respuesta.user = user
        respuesta.save()

    def crear_respuesta_opciones(self, parent_id, user_id):
        """!
        Metodo para crear una respuesta de selección simple y múltiple

        @author Rodrigo Boet (rboet at cenditel.gob.ve)
        @copyright GNU/GPLv2
        @date 28-03-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param parent_id <b>{int}</b> Recibe el número del id del padre
        @param user_id <b>{int}</b> Recibe el id del user
        @return Retorna los datos de contexto
        """
        user = User.objects.get(id=user_id)
        parent = Opcion.objects.get(pk=parent_id)
        respuesta = RespuestaOpciones()
        respuesta.opcion = parent
        respuesta.user = user
        respuesta.save()

    def crear_respuesta_abierta(self, parent_id, value,
                                user_id, es_justificacion=False):
        """!
        Metodo para crear una respuesta abierta

        @author Rodrigo Boet (rboet at cenditel.gob.ve)
        @copyright GNU/GPLv2
        @date 28-03-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param parent_id <b>{int}</b> Recibe el número del id del padre
        @param value <b>{str}</b> Recibe el valor de la respuesta
        @param user_id <b>{int}</b> Recibe el id del user
        @param es_justificacion <b>{bool}</b> Recibe el párametro que indica si es una justifiación
        @return Retorna los datos de contexto
        """
        user = User.objects.get(id=user_id)
        parent = Pregunta.objects.get(pk=parent_id)
        respuesta = RespuestaAbierta()
        respuesta.pregunta = parent
        respuesta.texto_respuesta = value
        respuesta.user = user
        respuesta.es_justificacion = es_justificacion
        respuesta.save()

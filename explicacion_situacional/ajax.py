# -*- coding: utf-8 -*-
"""
SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.ajax
#
# Ajax correspondientes a la explicacion situacional
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0
import json
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from explicacion_situacional.modelsEncuestas.modelsParticipacion import (
    RespuestaSino, RespuestaOpciones,
    RespuestaAbierta, RespuestaUbicacion
    )


def validar_participacion(request):
    """!
    Función que valida si un usuario ya participó en la consulta con un ente en particular

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright GNU/GPLv2
    @date 21-04-2017
    @param request <b>{object}</b> Objeto que contiene la petición
    @return Retorna un json con la respuesta
    """
    if not request.is_ajax():
        return JsonResponse({'mensaje': False, 'error': str('La solicitud no es ajax')})
    user = request.GET.get('user', None)
    consulta = request.GET.get('consulta', None)
    if(user and consulta):
        respuesta_sino = RespuestaSino.objects.filter(pregunta__consulta=consulta,user=user)
        respuesta_abierta = RespuestaAbierta.objects.filter(pregunta__consulta=consulta,user=user)
        respuesta_opciones = RespuestaOpciones.objects.filter(opcion__pregunta__consulta=consulta,user=user)
        if(respuesta_sino or respuesta_abierta or respuesta_opciones):
            return JsonResponse({'mensaje': True,'participacion':True})
        return JsonResponse({'mensaje': True,'participacion':False})
    else:
        return JsonResponse({'mensaje': False, 'error': str('No envío el \
                              usuario y/o el numero de la encuesta')})

# -*- coding: utf-8 -*-
"""
SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.views
#
# Vistas correspondientes a la explicacion situacional
# @author Ing. Erwin Paredes (eparedes at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

import time
import datetime 
from django.contrib import messages
from django.shortcuts import render, redirect

from explicacion_situacional.modelsEncuestas.modelsParticipacion import (
    RespuestaSino, RespuestaOpciones,
    RespuestaAbierta, RespuestaUbicacion
    )


def ParticipoCaracterizacionEconomica(request,pk):
    """!
    Chequea la participacion del usuario en la caracterización economica de la comunidad

    @author Ing. Erwin Leonel P.  (eparedes at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-005-2017
    @version 1.0.0
    """
    user = request.user
    if(user and pk):
        respuesta_sino = RespuestaSino.objects.filter(pregunta__consulta=pk,user=user)
        respuesta_abierta = RespuestaAbierta.objects.filter(pregunta__consulta=pk,user=user)
        respuesta_opciones = RespuestaOpciones.objects.filter(opcion__pregunta__consulta=pk,user=user)
        if(respuesta_sino or respuesta_abierta or respuesta_opciones):
            return redirect('explicacion:caracterizacion_economica')
        return redirect('explicacion:participar_encuesta_economica',pk=2)
    else:
        return redirect('explicacion:explicacion_situacional')
            
            
def ModificarRespuesta(request):
    if request.method == "POST":
        id = request.POST["ID"]
        respuesta = request.POST.get("respuesta")
        registro = RespuestaSino.objects.get(id=id)
        registro.respuesta = respuesta
        registro.save()
    return redirect('explicacion:caracterizacion_economica')


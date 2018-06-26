# -*- coding: utf-8 -*-
"""
SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.views.caracterizacionFisicaViews
#
# Vistas correspondientes a la explicacion situacional
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

import time
import datetime 
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import (
    FormView, UpdateView
)
from django.views.generic import (
    TemplateView, ListView
)

from explicacion_situacional.modelsEncuestas.modelsConsultas import (
    Consulta
    )
from explicacion_situacional.modelsExplicacion.modelsExplicacionesSituacional import (
    ExplicSitConsulta
    )
from explicacion_situacional.forms import ExplicacionForms

from utils.views import LoginRequeridoPerAuth

from explicacion_situacional.urls import *

from explicacion_situacional.modelsEncuestas.modelsParticipacion import (
    RespuestaSino, RespuestaOpciones,
    RespuestaAbierta, RespuestaUbicacion
    )


                        
class CaracterizacionEconomicaView(LoginRequeridoPerAuth, TemplateView):
    """!
    Clase que muestra el templates de la caracterización economica de la comunidad

    @author Ing. Erwin Leonel P.  (eparedes at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-005-2017
    @version 1.0.0
    """
    template_name = "caracterizacion.economica.html"
    group_required = [u"Administradores", u"Voceros", u"Integrantes"]



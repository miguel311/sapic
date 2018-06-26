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
from django.shortcuts import render
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


class ExplicacionSituacionalView(LoginRequeridoPerAuth, TemplateView):
    """!
    Clase que muestra el templates de la caracterización física de la comunidad

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-005-2017
    @version 1.0.0
    """
    template_name = "explicacion.situacional.html"
    group_required = [u"Administradores", u"Voceros", u"Integrantes"]


class CaracterizacionFisicaView(LoginRequeridoPerAuth, TemplateView):
    """!
    Clase que muestra el templates de la caracterización física de la comunidad

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-005-2017
    @version 1.0.0
    """
    template_name = "caracterizacion.fisica.html"
    group_required = [u"Administradores", u"Voceros", u"Integrantes"]


class RegisterUbicMapView(FormView):
    """!
    Clase que controla el formulario en la vista de la explicacion situacional

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 18-09-2017
    @version 1.0.0
    """
    form_class = ExplicacionForms
    template_name = 'map.explicacion.situacional.html'
    success_url = '/inicio/'

    def form_valid(self, form, **kwargs):
        """
        Funcion que valida el formulario de registro de la explicacion situacional
        @return: Dirige con un mensaje de exito a el home
        """
        ahora = int(time.strftime("%Y"))
        explicacion_anho = ExplicSitConsulta.objects.filter(fk_explicacion__fk_organizacion=form.cleaned_data['fk_organizacion'], 
                                         fecha__gt=datetime.date(ahora, 1, 1), fecha__lt=datetime.date(ahora, 12, 31)).exists()
        if explicacion_anho:
            self.success_url = '/ubicacion-geografica/'
            messages.error(self.request, "Error al agregar el mapa y la \
                                          ubicación cartográfica de \
                                          la organizacion social, ya se \
                                          registro la informacion para \
                                          de año")
            return super(RegisterUbicMapView, self).form_valid(form)
        else:
            cartografia = form.save()
            consultas = Consulta.objects.all()
            for consulta in consultas:
                exp_sit = ExplicSitConsulta()
                exp_sit.fk_consulta = Consulta.objects.get(pk=consulta.pk)
                exp_sit.fk_explicacion = cartografia
                exp_sit.save()
            messages.success(self.request, "Explicacion situacional, \
                                            registrada con exito")
            return super(RegisterUbicMapView, self).form_valid(form)

# -*- coding: utf-8 -*-
"""
SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.forms
#
# Formularios correspondientes a la explicacion situacional
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

from django.contrib.gis import forms
from django.forms.fields import (
    CharField
)

from explicacion_situacional.modelsExplicacion.modelsExplicacionesSituacional import *


class ExplicacionForms(forms.ModelForm):
    """!
    Clase que permite crear el formulario para la explicacion situacional

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """

    class Meta:
        """!
        Clase que construye los meta datos del formulario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 18-09-2017
        @version 1.0.0
        """
        model = ExplicacionSituacional
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """!
        Funcion que muestra el init del formulario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 18-09-2017
        """
        super(ExplicacionForms, self).__init__(*args, **kwargs)
        self.fields['fk_organizacion'].widget.attrs.update({
                                      'class': 'form-control'})
        self.fields['fk_organizacion'].empty_label = 'Seleccione la \
                                                     organizacion social'
        self.fields['fk_organizacion'].label = 'Organizacion Social'
        self.fields['fk_organizacion'].required = True

        self.fields['coordenadas'].widget = forms.OSMWidget.template_name = 'openlayers-es.html'
        self.fields['coordenadas'].widget = forms.OSMWidget(attrs={
                                    'default_zoom': 5.2, 'map_width': 600,
                                    'map_height': 400, 'default_lat': 8,
                                    'default_lon': -66})
        self.fields['coordenadas'].required = True

        self.fields['map_cartografico'].widget.attrs.update({'class':'form-control',
                                                   'data-show-preview':'true',
                                                   'accept':'image/*'})
        self.fields['map_cartografico'].label = 'Mapa cartografico'
        self.fields['map_cartografico'].required = True



class UbicacionForms(forms.Form):
    """!
    Clase que permite crear el formulario para el tipo de preguntas que requieren ubicacion

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 20-09-2017
    @version 1.0.0
    """
    ubicacion = CharField()

    class Meta:
        """!
        Clase que construye los meta datos del formulario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 18-09-2017
        @version 1.0.0
        """
        fields = ('ubicacion')

    def __init__(self, *args, **kwargs):
        """!
        Funcion que muestra el init del formulario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 18-09-2017
        """
        super(UbicacionForms, self).__init__(*args, **kwargs)
        
        self.fields['ubicacion'].widget = forms.OSMWidget.template_name = 'openlayers-es.html'
        self.fields['ubicacion'].widget = forms.OSMWidget(attrs={
                                    'default_zoom': 5.2, 'map_width': 600,
                                    'map_height': 400, 'default_lat': 8,
                                    'default_lon': -66})
        self.fields['ubicacion'].required = True

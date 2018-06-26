# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
"""!
Forms para generar los formulario del modulo organizaciones sociales

@author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 29-05-2017
@version 1.0.0
"""
from django import forms
from django.forms import (
    ModelForm,  modelform_factory, inlineformset_factory
    )

from .models import *

from utils.views import (
    obtenerEstados, listMunicipios
    )


class FormularioRegisterOrgSocial(ModelForm):
    """!
    Clase que permite crear el formulario para registrar organizaciones sociales

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    estados = obtenerEstados()
    municipios = listMunicipios()
    estado = forms.ChoiceField(required=True, choices=[("", "Seleccione Estado")] +
    [(est["id"], est["nombre"]) for est in estados])
    estado.widget.attrs.update({'class':'form-control'})
    municipio = forms.ChoiceField(required=True, choices=[("", "Seleccione Municipio")] +
    [(mun["id"], mun["nombre"]) for mun in municipios])
    municipio.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = OrganizacionSocial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormularioRegisterOrgSocial, self).__init__(*args, **kwargs)
        self.fields['fk_tipo_organizacion'].empty_label = 'Seleccione el Tipo De Organización'
        self.fields['fk_tipo_organizacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['fk_tipo_organizacion'].label= 'Tipo de Organización'
        self.fields['codigo'].widget.attrs.update({'class': 'form-control',
                                                   'placeholder': 'Código de la Organización Social'})
        self.fields['rif'].widget.attrs.update({'class': 'form-control',
                                                   'placeholder': 'R.I.F'})
        self.fields['situr'].widget.attrs.update({'class': 'form-control',
                                                   'placeholder': 'SITUR'})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control',
                                                   'placeholder': 'Nombre de la Organización Social'})
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                   'placeholder': 'Email de la Organización Social'})
        self.fields['fecha_conformacion'].widget.attrs.update(
                                            {'class': 'form-control',
                                             'placeholder':
                                             'Fecha de Conformación',
                                             'readonly':
                                             'readonly'})
        self.fields['sector'].widget.attrs.update({'class': 'form-control',
                                                   'placeholder': 'Sector de la Organización Social'})
        self.fields['localidad'].widget.attrs.update({'class': 'form-control'})
        self.fields['localidad'].label = 'Parroquia'
        self.fields['localidad'].empty_label = 'Seleccione la Parroquia'
        self.fields['activa'].widget.attrs.update({'class': 'form-control',
                                                   'data-toggle': 'toggle',
                                                   'data-on': 'Si',
                                                   'data-off': 'No',
                                                   'checked': 'checked'})
        self.fields['activa'].label = "¿La Organización se encuentra Activa?"


class FormularioVocero(ModelForm):
    """!
    Clase que crea el formulario para los objetivos especificos

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    class Meta:
        model = Vocero
        fields = ['fk_tipo_documento', 'nombres', 'apellidos', 'documento_identidad']

    def __init__(self, *args, **kwargs):
        super(FormularioVocero, self).__init__(*args, **kwargs)
        self.fields['fk_tipo_documento'].widget.attrs.update(
                                            {'class': 'form-control'})
        self.fields['fk_tipo_documento'].empty_label = 'Seleccione el Tipo De Documento'
        self.fields['fk_tipo_documento'].label = "Tipo de Documento"
        self.fields['nombres'].widget.attrs.update(
                                            {'class': 'form-control',
                                             'placeholder':
                                             'Nombres'})
        self.fields['apellidos'].widget.attrs.update(
                                            {'class': 'form-control',
                                             'placeholder':
                                             'Apellidos'})
        self.fields['documento_identidad'].widget.attrs.update(
                                            {'class': 'form-control',
                                             'placeholder':
                                             'Documento de Identidad'})

campos = ('fk_tipo_documento', 'nombres', 'apellidos', 'documento_identidad',)

FormsetObj = modelform_factory(Vocero, form=FormularioVocero, fields=campos)

FormsetVocero = inlineformset_factory(OrganizacionSocial, Vocero, form=FormsetObj,
                                                fields=campos, fk_name='fk_org_social',
                                                min_num=1, extra=0, validate_min=True,
                                                can_delete=True)
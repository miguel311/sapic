# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *
from .ajax import *

from .utils import obtenerOrganizaciones

urlpatterns = [
    url(r'^registrar-organizacion/$', RegisterOrgView.as_view(),
        name="registrar_organizacion"),
    url(r'^listar-organizacion/$', ListOrgView.as_view(),
        name="listar_organizacion"),

    # Ajax list Organizaciones, for Administradores
    url(r'^listar-organizaciones/$', ListOrgsAjaxView.as_view(),
        name="listar_orgs"),

    # Json que lista de objetos utiles realizados desde el modulo organizacion
    # social para los formularios
    url(r'^organizaciones_sociales/$', obtenerOrganizaciones,
        name='obtener_orgs'),
]

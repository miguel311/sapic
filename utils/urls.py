# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^inicio/$', StartView.as_view(), name='inicio'),
    url(r'^municipios/$', obtenerMunicipios, name='obtener_municipios'),
    url(r'^parroquias/$', obtenerParroquias, name='obtener_parroquias'),
    url(r'^comites/$', obtenerComitesbyUnidades, name='obtener_comites')
]

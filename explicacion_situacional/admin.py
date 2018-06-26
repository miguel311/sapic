from django.contrib.gis import admin as adminGeo
from django.contrib import admin
from explicacion_situacional.modelsEncuestas.modelsConsultas import *
from explicacion_situacional.modelsEncuestas.modelsParticipacion import *
from explicacion_situacional.modelsExplicacion.modelsExplicacionesSituacional import *


admin.site.register(Caracterizacion)
admin.site.register(Consulta)
admin.site.register(TipoPregunta)
admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(RespuestaSino)
admin.site.register(RespuestaOpciones)
admin.site.register(RespuestaAbierta)
admin.site.register(RespuestaUbicacion)
admin.site.register(ExplicacionSituacional, adminGeo.OSMGeoAdmin)
admin.site.register(ExplicSitConsulta)

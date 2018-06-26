from django.contrib.auth.models import User, Group
from rest_framework import serializers
from explicacion_situacional.models import ExplicacionSituacional, ExplicSitConsulta
from explicacion_situacional.modelsEncuestas.modelsParticipacion import (
    RespuestaSino, RespuestaOpciones,
    RespuestaAbierta, RespuestaUbicacion
    )
from explicacion_situacional.modelsEncuestas.modelsConsultas import Pregunta
import django_filters.rest_framework


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="serializer:user-detail")
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="serializer:group-detail")
    class Meta:
        model = Group
        fields = ('url', 'name')


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'
    
    
class RespuestaSiNoSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    pregunta = PreguntaSerializer(many=False, read_only=True)

    class Meta:
        model = RespuestaSino
        fields = ('id','pregunta', 'respuesta', 'user')
        filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)   

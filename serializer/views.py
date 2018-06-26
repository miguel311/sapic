from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializer.serializers import UserSerializer, GroupSerializer, RespuestaSiNoSerializer
from explicacion_situacional.models import ExplicacionSituacional, ExplicSitConsulta
from explicacion_situacional.modelsEncuestas.modelsParticipacion import (
    RespuestaSino, RespuestaOpciones,
    RespuestaAbierta, RespuestaUbicacion
    )
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    
class RespuestaSiNoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    #queryset = RespuestaSino.objectgenerics.ListAPIViews.all()
    serializer_class = RespuestaSiNoSerializer
    
    def get_queryset(self):
        """
        This view should return a list of all the Preguntas
        for the currently authenticated user.
        """
        user = self.request.user
        return RespuestaSino.objects.filter(user=user)


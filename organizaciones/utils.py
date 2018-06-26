import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

from .models import *


def listOrganizaciones():
    """
    Función que permite obtener la lista de Organizaciones

    El método hace una lista consultando el modelo Organizacion Social

    @return: Lista de Organizaciones
    """
    try:
        if OrganizacionSocial.objects.exists():
            consulta = OrganizacionSocial.objects.all().values('id', 'nombre')
        else:
            consulta = [{'id': '', 'nombre': ''}]
    except:
        consulta = [{'id': '', 'nombre': ''}]

    return consulta


def obtenerOrganizaciones(request):
    """
    Función que permite obtener la lista de organizaciones dado un tipo de organizacion

    El método hace un llamado al modelo para realizar una consulta

    @param fk_tipo: Identificador del tipo de organizacion
    @type fk_tipo: entero

    @return: Lista de organizaciones de acuerdo al tipo de organizacion
    """

    try:
        if OrganizacionSocial.objects.exists():
            fk_tipo = request.GET.get('fk_tipo')
            #print (fk_tipo)
            organizaciones = OrganizacionSocial.objects.filter(fk_tipo_organizacion=fk_tipo).values('id', 'nombre')
            #print (organizaciones)
            data = json.dumps(list(organizaciones), cls=DjangoJSONEncoder)
            print (data)
        else:
            data = {}
    except:
        data = {}

    return HttpResponse(data, content_type='application/json')

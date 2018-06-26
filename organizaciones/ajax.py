# -*- encoding: utf-8 -*-
from django.conf import settings
from django_datatables_view.base_datatable_view import BaseDatatableView
from organizaciones.models import (
    OrganizacionSocial
    )
from users.models import (
    UserProfileVocero
    )
from utils.views import (
    LoginRequeridoPerAuth
)

class ListOrgsAjaxView(LoginRequeridoPerAuth, BaseDatatableView):
    """!
    Prepara la data para mostrar en el datatable

    @author Ing. Erwin Leonel P. (eparedes at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 08-08-2017
    @version 1.0.0
    """
    # The model we're going to show
    model = OrganizacionSocial
    # define the columns that will be returned
    columns = ['pk','fk_tipo_organizacion','codigo','rif','situr','nombre',
               'email','fecha_conformacion','sector','localidad','activa']
    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['pk', 'codigo', 'rif', 'situr']
    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500
    group_required = [u"Administradores", u"Voceros"]

    def __init__(self):
        super(ListOrgsAjaxView, self).__init__()

    def get_initial_queryset(self):
        """!
        Consulta el modelo OrganizacionSocial

        @return: Objeto de la consulta
        """
        # return queryset used as base for futher sorting/filtering
        # these are simply objects displayed in datatable
        # You should not filter data returned here by any filter values entered by user. This is because
        # we need some base queryset to count total number of records.
        user = self.request.user
        try:
            grupos = user.groups.all()
            grupo = []
            if len(grupos) > 1:
                for g in grupos:
                    grupo += str(g),
            else:
                grupo = str(user.groups.get())
        except:
            grupo = "No pertenece a un grupo"
        if "Administradores" in grupo:
            return self.model.objects.all()
        elif "Voceros" in grupo:
            try:
                usuario_vocero = UserProfileVocero.objects.select_related().get(fk_user=user)
            except UserProfileVocero.DoesNotExist:
                usuario_vocero = None
            return self.model.objects.select_related().filter(vocero__documento_identidad=usuario_vocero.fk_vocero.documento_identidad)

    def prepare_results(self, qs):
        """!
        Prepara la data para mostrar en el datatable
        @return: Objeto json con los datos de los usuarios
        """
        # prepare list with output column data
        json_data = []
        for item in qs:
            org = "<a data-toggle='modal' data-target='#myModal' \
                    class='btn btn-block btn-info btn-xs fa fa-edit' \
                    onclick='modal_org(%s)'>%s</a>\
                    " % (str(item.pk), str(item.fk_tipo_organizacion.tipo))
            if item.fecha_conformacion:
                fecha_conformacion = item.fecha_conformacion.strftime("%Y-%m-%d")
            else:
                fecha_conformacion = "No ha ingresado"
            if item.activa:
                activo = "Activo"
                activar = "<input type='checkbox' id='org-" + str(item.pk) + "' value='" + str(item.pk) + "' name='inactivar' onclick='$(\"#forma_activar\").submit();'/>\
                            <label for='org-" + str(item.pk) + "'>\
                                <img  src='" + settings.MEDIA_URL +\
                                "imagenes/inactivar.png' id='inactivo'\
                                title='Inactivar Organización' \
                                />\
                            </label>"

            else:
                activo = "Inactivo"
                activar = "<input type='checkbox' id='org-" + str(item.pk) + "' value='" + str(item.pk) + "' name='activar' onclick='$(\"#forma_activar\").submit();'/>\
                            <label for='org-" + str(item.pk) + "'>\
                                <img  src='" + settings.MEDIA_URL + \
                                "imagenes/activar.png' id='activo' \
                                title='Activar Organización'/>\
                            </label>"
            json_data.append([
                org,
                item.codigo,
                item.rif,
                item.situr,
                item.nombre.title(),
                item.email,
                fecha_conformacion,
                item.sector,
                activo,
                str(item.localidad),
                activar
            ])
            grupo = ""
        return json_data

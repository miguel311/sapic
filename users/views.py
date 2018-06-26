# -*- coding: utf-8 -*-
"""!
Vista que controla los procesos de los usuarios

@author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 29-05-2017
@version 1.0.0
"""

from django.shortcuts import render
from django import forms
from django.db.models import Q
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import (
    authenticate, logout, login
)

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth.models import (
    Group, Permission, User
)
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import (
    reverse_lazy, reverse
)
from django.core.validators import validate_email

from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.views.generic import (
    TemplateView, ListView
)
from django.views.generic.base import RedirectView
from django.views.generic.edit import (
    FormView, UpdateView
)
from multi_form_view import MultiModelFormView

from utils.views import LoginRequeridoPerAuth

from .forms import *

from organizaciones.models import VoceroComite

from .models import (
    UserProfile, UserProfileVocero
    )


class LoginView(FormView):
    """!
    Muestra el formulario de ingreso a la aplicación

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    form_class = FormularioLogin
    template_name = 'users.login.html'
    success_url = '/inicio/'

    def form_valid(self, form):
        """
        Valida el formulario de logeo
        @return: Dirige a la pantalla inicial de la plataforma
        """
        usuario = form.cleaned_data['usuario']
        contrasena = form.cleaned_data['contrasena']

        try:
            validate_email(usuario)
            try:
                usuario = User.objects.get(email=usuario).username
                valid_email = True
            except:
                messages.error(self.request, 'No existe este correo: %s \
                                              asociado a una cuenta' % (usuario))
        except:
            valid_email = False

        usuario = authenticate(username=usuario, password=contrasena)
        if usuario is not None:
            login(self.request, usuario)
            self.request.session['permisos'] = list(usuario.get_all_permissions())
            try:
                grupos = usuario.groups.all()
                grupo = []
                if len(grupos) > 1:
                    for g in grupos:
                        grupo += str(g),
                else:
                    grupo = str(usuario.groups.get())
            except:
                grupo = "No pertenece a un grupo"

            self.request.session['grupos'] = grupo

            if self.request.POST.get('remember_me') is not None:
                # Session expira a los dos meses si no se deslogea
                self.request.session.set_expiry(1209600)
            messages.info(self.request, 'Bienvenido %s has ingresado a el \
                                         SAPIC con el usuario %s \
                                         ' % (usuario.first_name,
                                              usuario.username))
        else:
            user = User.objects.filter(username=form.cleaned_data['usuario'])
            if user:
                user = user.get()
                if not user.is_active:
                    self.success_url = reverse_lazy('users:login')
                    messages.error(self.request, 'La cuenta esta inactiva \
                                                consulte con un adminitrador')
                else:
                    self.success_url = reverse_lazy('users:login')
                    messages.warning(self.request, 'Verifique su nombre y contraseña\
                                                 y vuelve a intertar')

        return super(LoginView, self).form_valid(form)


class PasswordChangeView(LoginRequeridoPerAuth, SuccessMessageMixin,
                         PasswordChangeView):
    """!
    Cambiar la Contraseña

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 20-07-2017
    @version 1.0.0
    """
    template_name = 'users.change.pass.html'
    form_class = PasswordChangeForm
    success_url = '/inicio/'
    success_message = "Cambio de contraseña con exito"
    group_required = [u"Administradores", u"Voceros", u"Integrantes"]


class LogOutView(RedirectView):
    """!
    Salir de la apliacion

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    permanent = False
    query_string = True

    def get_redirect_url(self):
        """!
        Dirige a la pantalla del login
        @return: A la url del login
        """
        logout(self.request)
        return reverse_lazy('users:login')


class OthersOptionsView(LoginRequeridoPerAuth, TemplateView):
    """!
    Clase que muestra el templates de las opciones del usuario

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-005-2017
    @version 1.0.0
    """
    template_name = "users.other.options.html"
    group_required = [u"Administradores", u"Voceros", u"Integrantes"]


class RegisterView(LoginRequeridoPerAuth, MultiModelFormView):
    """!
    Muestra el formulario de registro de usuarios

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    template_name = "users.register.html"
    form_classes = {
      'user': FormularioAdminRegistro,
      'user_perfil': FormularioAdminRegPerfil,
    }
    success_url = reverse_lazy('utils:inicio')
    model = Group
    model_permi = Permission
    group_required = [u"Administradores"]
    record_id=None

    def get_context_data(self, **kwargs):
        """
        Carga el formulario en la vista,para registrar usuarios
        @return: El contexto con los objectos para la vista
        """
        return super(RegisterView, self).get_context_data(**kwargs)

    def forms_valid(self, forms, **kwargs):
        """
        Valida el formulario de registro del perfil de usuario
        @return: Dirige con un mensaje de exito a el home
        """
        nuevo_usuario = forms['user'].save()
        nuevo_perfil = forms['user_perfil'].save(commit=False)
        nuevo_perfil.fk_user = nuevo_usuario
        nuevo_perfil.save()
        usuario = forms['user'].cleaned_data['username']
        grupos = forms['user'].cleaned_data['groups']
        for group in grupos:
            # Agrega a el usuario al(los) grupo(s) seleccionado(s)
            nuevo_usuario.groups.add(group.pk)
        model_user = ContentType.objects.get_for_model(User).pk
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=model_user,
            object_id=nuevo_usuario.id,
            object_repr=str(nuevo_usuario.username),
            action_flag=ADDITION)
        messages.success(self.request, "Usuario %s creado con exito\
                                       " % (str(usuario)))
        return super(RegisterView, self).forms_valid(forms)


class DataDetailView(LoginRequeridoPerAuth, ListView):
    """!
    Consultar los datos basicos del usuario
    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 21-07-2017
    @version 1.0.0
    """
    template_name = 'users.data.detail.html'
    model = UserProfileVocero
    group_required = [u"Voceros"]

    def dispatch(self, request, *args, **kwargs):
        if int(request.user.pk) != int(self.kwargs.get('pk', None)):
            return redirect('utils:403error')
        return super(DataDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Carga el formulario en la vista,para registrar usuarios
        @return: El contexto con los objectos para la vista
        """
        context = super(DataDetailView, self).get_context_data(**kwargs)
        self.record_id = self.kwargs.get('pk', None)
        try:
            record = self.model.objects.select_related().get(fk_user=self.record_id)
        except User.DoesNotExist:
            record = None
        if record.fk_vocero.fk_rol_unidad.pk == 1:
            try:
                comite = VoceroComite.objects.get(fk_vocero=record.fk_vocero)
            except:
                comite = {}
                comite['fk_comite'] = "Este vocero no fue asignado a un comite"
        else:
            comite = None
        context['upUser'] = record
        context['comite'] = comite
        return context


class UpdatePerfilAdmin(LoginRequeridoPerAuth, MultiModelFormView):
    """!
    Actualizar el perfil del usuario

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 31-01-2017
    @version 1.0.0
    """
    model = UserProfile
    form_classes = {
      'user': FormularioUpdate,
      'user_perfil': FormularioAdminRegPerfil,
    }
    template_name = 'users.update.perfil.html'
    success_url = reverse_lazy('users:options')
    group_required = [u"Administradores"]
    record_id = None

    def dispatch(self, request, *args, **kwargs):
        if int(request.user.pk) != int(self.kwargs.get('pk', None)):
            return redirect('utils:403error')
        return super(UpdatePerfilAdmin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Carga el formulario en la vista,para registrar usuarios
        @return: El contexto con los objectos para la vista
        """
        context = super(UpdatePerfilAdmin, self).get_context_data(**kwargs)
        self.record_id = self.kwargs.get('pk', None)
        try:
            record = self.model.objects.select_related().get(fk_user=self.record_id)
        except User.DoesNotExist:
            record = None
        context['upUser'] = record
        return context

    def get_objects(self, **kwargs):
        """
        Carga el formulario en la vista,para actualizar el perfil del  usuario
        @return: El contexto con los objectos para la vista
        """
        self.record_id = self.kwargs.get('pk', None)
        try:
            record = self.model.objects.select_related().get(fk_user=self.record_id)
        except User.DoesNotExist:
            record = None
        return {
          'user_perfil': record,
          'user': record.fk_user if record else None}

    def forms_valid(self, forms, **kwargs):
        """
        Valida el formulario de registro del perfil de usuario
        @return: Dirige con un mensaje de exito a el home
        """
        self.record_id = self.kwargs.get('pk', None)
        objeto = get_object_or_404(User, pk=self.record_id)
        if self.record_id is not None:
            messages.success(self.request, "Usuario %s Actualizado con exito\
                                           " % (str(objeto.username)))
        return super(UpdatePerfilAdmin, self).forms_valid(forms)


class DataDetailAdminView(LoginRequeridoPerAuth, ListView):
    """!
    Consultar los datos basicos del usuario
    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 21-07-2017
    @version 1.0.0
    """
    template_name = 'users.data.detail.html'
    model = UserProfile
    group_required = [u"Administradores"]

    def dispatch(self, request, *args, **kwargs):
        if int(request.user.pk) != int(self.kwargs.get('pk', None)):
            return redirect('utils:403error')
        return super(DataDetailAdminView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Carga el formulario en la vista,para registrar usuarios
        @return: El contexto con los objectos para la vista
        """
        context = super(DataDetailAdminView, self).get_context_data(**kwargs)
        self.record_id = self.kwargs.get('pk', None)
        try:
            record = self.model.objects.select_related().get(fk_user=self.record_id)
        except User.DoesNotExist:
            record = None
        context['upUser'] = record
        return context

    def forms_valid(self, forms, **kwargs):
        """
        Valida el formulario de registro del perfil de usuario
        @return: Dirige con un mensaje de exito a el home
        """
        self.record_id = self.kwargs.get('pk', None)
        objeto = get_object_or_404(User, pk=self.record_id)
        if self.record_id is not None:
            messages.success(self.request, "Usuario %s Actualizado con exito\
                                           " % (str(objeto.username)))
        return super(UpdatePerfilAdmin, self).forms_valid(forms)


class ListUsersView(LoginRequeridoPerAuth, TemplateView):
    """!
    Listar usuarios de la plataforma

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-05-2017
    @version 1.0.0
    """
    template_name = "users.list.html"
    model = User
    success_url = reverse_lazy('users:lista_users')
    group_required = [u"Administradores"]

    def __init__(self):
        super(ListUsersView, self).__init__()

    def post(self, *args, **kwargs):
        '''
        Cambia el estado activo a el usuario
        @return: Dirige a la tabla que muestra los usuarios de la apliacion
        '''
        accion = self.request.POST
        activar = accion.get('activar', None)
        inactivar = accion.get('inactivar', None)
        estado = False

        if activar is not None:
            user = activar
            estado = True
        elif inactivar is not None:
            user = inactivar
            estado = False
        else:
            messages.error(self.request, "Esta intentando hacer \
                                          una accion incorrecta")
        try:
            user_act = self.model.objects.get(pk=user)
            user_act.is_active = estado
            user_act.save()
            if estado:
                messages.success(self.request, "Se ha activado \
                                                el usuario: %s\
                                                " % (str(user_act)))
            else:
                messages.warning(self.request, "Se ha inactivado \
                                                el usuario: %s\
                                                " % (str(user_act)))
        except:
            messages.info(self.request, "El usuario no existe")
        return redirect(self.success_url)


class ModalsPerfil(LoginRequeridoPerAuth, MultiModelFormView):
    """!
    Construye el modals para la actualizacion del usuario

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 31-01-2017
    @version 1.0.0
    """
    model = UserProfile
    form_classes = {
      'user': FormularioAdminUpdate,
      'user_perfil': FormularioAdminRegPerfil,
    }
    template_name = 'users.modals.perfil.html'
    success_url = reverse_lazy('users:lista_users')
    group_required = [u"Administradores"]
    record_id = None

    def get_context_data(self, **kwargs):
        """
        Carga el formulario en la vista, para registrar usuarios
        @return: El contexto con los objectos para la vista
        """
        context = super(ModalsPerfil, self).get_context_data(**kwargs)
        self.record_id = self.kwargs.get('pk', None)
        if self.record_id is not None:
            try:
                usuario = User.objects.get(pk=self.record_id)
            except User.DoesNotExist:
                usuario = None
            try:
                record = self.model.objects.select_related().get(fk_user=self.record_id)
            except self.model.DoesNotExist:
                if usuario is not None:
                    try:
                        record = UserProfileVocero.objects.select_related().get(fk_user=self.record_id)
                    except:
                        record = None
        context['upUser'] = record
        return context

    def get_objects(self, **kwargs):
        """
        Carga el formulario en la vista,para actualizar el perfil del  usuario
        @return: El contexto con los objectos para la vista
        """
        self.record_id = self.kwargs.get('pk', None)
        if self.record_id is not None:
            try:
                usuario = User.objects.get(pk=self.record_id)
            except User.DoesNotExist:
                usuario = None
            try:
                record = self.model.objects.select_related().get(fk_user=self.record_id)
                vocero = None
                self.form_classes['user_perfil'] = FormularioAdminRegPerfil
            except self.model.DoesNotExist:
                if usuario is not None:
                    try:
                        vocero = UserProfileVocero.objects.select_related().get(fk_user=self.record_id)
                        self.form_classes['user_perfil'] = FormupdatePerfilVoceros
                    except UserProfileVocero.DoesNotExist:
                        vocero = None
                record = None
        return {
          'user_perfil': vocero.fk_vocero if vocero else record,
          'user': record.fk_user if record else vocero.fk_user }

    def get_success_url(self):
        return reverse('users:lista_users')

    def forms_valid(self, forms, **kwargs):
        """
        Valida el formulario de registro del perfil de usuario
        @return: Dirige con un mensaje de exito a el home
        """
        self.record_id = self.kwargs.get('pk', None)
        if self.record_id is not None:
            objeto = get_object_or_404(User, pk=self.record_id)
            messages.success(self.request, "Usuario %s Actualizado con exito\
                                           " % (str(objeto.username)))
        return super(ModalsPerfil, self).forms_valid(forms)


class UpdatePerfil(LoginRequeridoPerAuth, MultiModelFormView):
    """!
    Actualizar el perfil del usuario

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 31-01-2017
    @version 1.0.0
    """
    model = UserProfileVocero
    form_classes = {
      'user': FormularioUpdate,
      'user_perfil': FormularioRegVoceros,
    }
    template_name = 'users.update.perfil.html'
    success_url = reverse_lazy('users:options')
    group_required = [u"Voceros"]
    record_id = None

    def dispatch(self, request, *args, **kwargs):
        if int(request.user.pk) != int(self.kwargs.get('pk', None)):
            return redirect('utils:403error')
        return super(UpdatePerfil, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Carga el formulario en la vista, para registrar usuarios
        @return: El contexto con los objectos para la vista
        """
        context = super(UpdatePerfil, self).get_context_data(**kwargs)
        self.record_id = self.kwargs.get('pk', None)
        try:
            record = self.model.objects.select_related().get(fk_user=self.record_id)
        except User.DoesNotExist:
            record = None
        context['upUser'] = record
        return context

    def get_objects(self, **kwargs):
        """
        Carga el formulario en la vista,para actualizar el perfil del  usuario
        @return: El contexto con los objectos para la vista
        """
        self.record_id = self.kwargs.get('pk', None)
        try:
            record = self.model.objects.select_related().get(fk_user=self.record_id)
        except User.DoesNotExist:
            record = None
        return {
          'user_perfil': record.fk_vocero,
          'user': record.fk_user if record else None}

    def forms_valid(self, forms, **kwargs):
        """
        Valida el formulario de registro del perfil de usuario
        @return: Dirige con un mensaje de exito a el home
        """
        self.record_id = self.kwargs.get('pk', None)
        objeto = get_object_or_404(User, pk=self.record_id)
        if self.record_id is not None:
            messages.success(self.request, "Usuario %s Actualizado con exito\
                                           " % (str(objeto.username)))
        return super(UpdatePerfil, self).forms_valid(forms)


class RegisterVocerosView(LoginRequeridoPerAuth, MultiModelFormView):
    """!
    Muestra el formulario de registro de usuarios voceros

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    model = UserProfileVocero
    form_classes = {
      'user': FormularioAdminRegVoceros,
      'user_vocero': FormularioRegVoceros,
    }
    template_name = 'users.register.vocero.html'
    success_url = reverse_lazy('users:options')
    group_required = [u"Administradores"]
    record_id = None


    def get_objects(self, **kwargs):
        """
        Carga el formulario en la vista,para actualizar el perfil del  usuario
        @return: El contexto con los objectos para la vista
        """
        self.record_id = self.kwargs.get('pk', None)
        try:
            record = self.model.objects.select_related().get(fk_user=self.record_id)
        except self.model.DoesNotExist:
            record = None
        return {
          'user_vocero': record,
          'user': record.fk_user if record else None}

    def forms_valid(self, forms, **kwargs):
        """
        Valida el formulario del perfil de vocero y usuario
        @return: Dirige con un mensaje de exito al registro de proyecto
        """
        # Campos para instanciar el vocero y actualizar sus campos
        documento_identidad = forms['user_vocero'].cleaned_data['documento']
        tipo_documento = forms['user_vocero'].cleaned_data['fk_tipo_documento']
        organizacion_social = forms['user_vocero'].cleaned_data['organizacion']
        comite = forms['user_vocero'].cleaned_data['comite_unidad_ejecutiva']

        # Verifica si el vocero tiene registro sobre la organizacion social
        try:
            vocero = Vocero.objects.get(fk_org_social=organizacion_social,
                                        fk_tipo_documento=tipo_documento,
                                        documento_identidad=documento_identidad)
            actualizar_vocero = self.form_classes['user_vocero'](
                                self.request.POST,
                                instance=vocero)
            actualizar_vocero.save(commit=False)

            # Crea el nuevo usuario a partir del formulario
            nuevo_usuario = forms['user'].save()
            # Agrega al grupo de voceros al nuevo usuario
            nuevo_usuario.groups.add(Group.objects.get(pk=2))
            # Actualiza los datos del vocero a parit de la instancia del formulario
            vocero_actualizado = actualizar_vocero.save()
            # Asocia el vocero con la nueva cuenta de usuario
            asociar_voceros = self.model(fk_user=nuevo_usuario,
                                         fk_vocero=vocero_actualizado)
            # Si el usuario pertenece a un comite lo asocia
            if comite is not None:
                try:
                    # Asocia el vocero con un comite de la unidad Ejecutiva
                    comite_unidad = VoceroComite(fk_vocero=vocero_actualizado,
                                                 fk_comite=comite)
                    comite_unidad.save()
                except:
                    messages.warning(self.request, "Existe un problema al \
                                                    relacionar el comite a \
                                                    este vocero")
            try:
                # Crea la cuenta de usuario vocero
                asociar_voceros.save()
                nombre_vocero = str(vocero_actualizado.nombres) + " \
                                " + str(vocero_actualizado.apellidos)
                messages.success(self.request, "Se creo el usuario %s, para el \
                                                vocero %s" % (
                                                nuevo_usuario.username,
                                                nombre_vocero))
            except:
                messages.error(self.request, "El voceros al que quieres asociar  \
                                              a la cuenta ya existe o ya se \
                                              encuentra asociado")
                return redirect(self.success_url)

        except:
            messages.error(self.request, "Este Vocero %s, no se encuentra \
                                          asociado a esta organizacion: %s" % (
                                          documento_identidad,
                                          organizacion_social.nombre))
            return redirect(self.success_url)

        return redirect(self.success_url)

    def forms_invalid(self, forms, **kwargs):

        return super(RegisterVocerosView, self).forms_invalid(forms)

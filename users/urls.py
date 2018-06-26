# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import (
    password_reset, password_reset_done,
    )

from .views import *
from .ajax import *
from .forms import PasswordResetForm, PasswordChangeForm

urlpatterns = [
    # Login and Logut all users
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogOutView.as_view(), name="logout"),

    # Reset password all users
    url(r'^accounts/password/reset/$', password_reset,
        {'post_reset_redirect': '/accounts/password/done/',
         'template_name': 'base.forget.html',
         'password_reset_form': PasswordResetForm},
        name="forget"),
    url(r'^accounts/password/done/$', password_reset_done,
        {'template_name': 'base.passreset.done.html'},
        name='reset_done'),

    # Options Users, for all users
    url(r'^otras-opciones/$', OthersOptionsView.as_view(), name="options"),
    url(r'^cambiar-password/$', PasswordChangeView.as_view(),
     name="change_password"),
    url(r'^mis-datos/(?P<pk>\d+)/$', DataDetailView.as_view(),
     name="data_detail"),
    url(r'^modificar-mis-datos/(?P<pk>\d+)/$', UpdatePerfil.as_view(),
     name="update_perfil"),

    # Urls Access Administradores
    url(r'^lista-usuarios/$', ListUsersView.as_view(), name="lista_users"),
    url(r'^perfil/(?P<pk>\d+)/$', ModalsPerfil.as_view(),
        name="modal_perfil"),
    url(r'^registrar/$', RegisterView.as_view(), name="registrar"),
    url(r'^modificar-mis-datos-admin/(?P<pk>\d+)/$', UpdatePerfilAdmin.as_view(), name="update_perfil_admin"),
    url(r'^mis-datos-admin/(?P<pk>\d+)/$', DataDetailAdminView.as_view(),
     name="data_detail_admin"),
    url(r'^registrar-voceros/$', RegisterVocerosView.as_view(), name="registrar_voceros"),


    # Ajax list Users, for Administradores
    url(r'^listar-usuarios/$', ListUsersAjaxView.as_view(),
        name="listar_users"),
]

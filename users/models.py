# -*- coding: utf-8 -*-
"""!
Modelo que construye los modelos de datos del usuario

@author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 18-01-2017
@version 1.0.0
"""

from django.db import models
from django.contrib.auth.models import (
    Group, User
    )

from utils.models import (
    TipoDocumento,
    )

from organizaciones.models import (
    Vocero,
    )

"""
Se agrega un campo de descripcion al modelo group para describir el grupo de usuarios
"""
Group.add_to_class('descripcion', models.TextField(blank=True))


class UserProfile(models.Model):
    """!
    Clase que construye el modelo de datos para el perfil de usuario

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 18-01-2017
    @version 1.0.0
    """
    fk_user = models.OneToOneField(User)
    fk_tipo_documento = models.ForeignKey(TipoDocumento)
    id_perfil = models.CharField(unique=True, max_length=12,
                                 verbose_name='Documento de identidad')

    class Meta:
        """!
        Clase que construye los meta datos del modelo

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 18-01-2017
        @version 1.0.0
        """
        ordering = ('fk_user',)
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuarios'
        db_table = 'users_perfil'

    def __str__(self):
        """!
        Funcion que muestra el dato del perfil de usuario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 18-01-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve el objeto del perfil de usuario
        """
        return self.fk_user.username


class UserProfileVocero(models.Model):
    """!
    Clase que construye el modelo de datos para el perfil de usuario vocero

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 03-08-2017
    @version 1.0.0
    """
    fk_user = models.OneToOneField(User)
    fk_vocero = models.OneToOneField(Vocero)

    class Meta:
        """!
        Clase que construye los meta datos del modelo

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 03-08-2017
        @version 1.0.0
        """
        ordering = ('fk_user',)
        verbose_name = 'Perfil de usuario vocero'
        verbose_name_plural = 'Perfiles de usuarios voceros'
        db_table = 'users_perfil_vocero'

    def __str__(self):
        """!
        Funcion que muestra el dato del perfil de usuario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 03-08-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve el objeto del perfil de usuario
        """
        return self.fk_user.username

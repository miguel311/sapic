# -*- coding: utf-8 -*-
"""!
Modelo que construye el modelo de datos de las utilidades

@author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 18-01-2017
@version 1.0.0
"""
from django.db import models
from django.contrib.gis.db import models


class Pais(models.Model):
    """!
    Clase que contiene el modelo de datos de Pais

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    nombre = models.CharField(max_length=50)
    location = models.PointField(help_text="Representa (Latitud, Longitud)")

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nombre



class Estado(models.Model):
    """!
    Clase que contiene el modelo de datos del Estado

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais)
    location = models.PointField(help_text="Representa (Latitud, Longitud)")


    class Meta:
        ordering = ('nombre',)
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    """!
    Clase que contiene el modelo de datos del Municipio

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    nombre = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado)
    location = models.PointField(help_text="Representa (Latitud, Longitud)")

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.nombre


class Parroquia(models.Model):
    """!
    Clase que contiene el modelo de datos de la parroquia

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    nombre = models.CharField(max_length=50)
    municipio = models.ForeignKey(Municipio)
    location = models.PointField(help_text="Representa (Latitud, Longitud)")

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'

    def __str__(self):
        return self.nombre


class TipoDocumento(models.Model):
    """!
    Clase que contiene el tipo de documento

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    abreviatura = models.CharField(max_length=4, verbose_name='Acrónimo')
    descripcion = models.TextField()

    class Meta:
        ordering = ('abreviatura',)
        verbose_name = 'Tipo Documento'
        verbose_name_plural = 'Tipos Documentos'

    def __str__(self):
        return self.abreviatura


class Nacionalidad(models.Model):
    """!
    Clase que contiene el modelo de datos para la Nacionalidad

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    fk_pais = models.ForeignKey(Pais, verbose_name='Pais')
    tipo_nacionalidades = models.CharField(max_length=128)
    abreviatura = models.CharField(max_length=3)

    class Meta:
        ordering = ('tipo_nacionalidades',)
        verbose_name = 'Nacionalidad'
        verbose_name_plural = 'Nacionalidades'

    def __str__(self):
        return self.tipo_nacionalidades


class EstadoCivil(models.Model):
    """!
    Clase que contiene el modelo de datos para el Estado CIvil

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    estado_civiles = models.CharField(max_length=50)

    class Meta:
        ordering = ('estado_civiles',)
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estado Civil'

    def __str__(self):
        return self.estado_civiles


class Parentesco(models.Model):
    """!
    Clase que contiene el modelo de datos para los Parentescos

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    parentescos = models.CharField(max_length=50)

    class Meta:
        ordering = ('parentescos',)

    def __str__(self):
        return self.parentescos


class TipoEnfermedad(models.Model):
    """!
    Clase que contiene el modelo de datos para los tipos de Enfermedades

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    tipo_enfermedades = models.CharField(max_length=500, unique=True)
    causa = models.TextField()
    activa = models.BooleanField(default=True)

    class Meta:
        ordering = ('tipo_enfermedades',)
        verbose_name = 'Tipo Enfermedad'
        verbose_name_plural = 'Tipo Enfermedades'

    def __str__(self):
        return self.tipo_enfermedades


class TipoTrabajo(models.Model):
    """!
    Clase que contiene el modelo de datos para los Tipos de Trabajos

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    tipo_trabajos = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ('tipo_trabajos',)
        verbose_name = 'Tipo Trabajo'
        verbose_name_plural = 'Tipos de Trabajo'

    def __str__(self):
        return self.tipo_trabajos


class CondicionVivienda(models.Model):
    """!
    Clase que contiene el modelo de datos para la Condicion de Vivienda

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    condiciones = models.CharField(max_length=50)

    class Meta:
        ordering = ('condiciones',)
        verbose_name = 'Condicion de la Vivienda'
        verbose_name_plural = 'Condiciones de las Viviendas'

    def __str__(self):
        return self.condiciones


class EstadoVivienda(models.Model):
    """!
    Clase que contiene el modelo de datos para el Estado de Vivienda

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    estado = models.CharField(max_length=50)

    class Meta:
        ordering = ('estado',)
        verbose_name = 'Estado de la Vivienda'
        verbose_name_plural = 'Estados de las Viviendas'

    def __str__(self):
        return self.estado


class TipoServicio(models.Model):
    """!
    Clase que contiene el modelo de datos para los Tipos de Servicios

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    tipos = models.CharField(max_length=50)

    class Meta:
        ordering = ('tipos',)

    def __str__(self):
        return self.tipos


class CalidadServicio(models.Model):
    """!
    Clase que contiene el modelo de datos para la Calidad de los servicios

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    estatus = models.CharField(max_length=50)

    class Meta:
        ordering = ('estatus',)
        verbose_name = 'Calidad del Servicio'
        verbose_name_plural = 'Calidad de los Servicios'

    def __str__(self):
        return self.estatus


class UnidadesOrganizacionSocial(models.Model):
    """!
    Clase que contiene el modelo de datos para Las Unidades de la Organizacion Social

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    tipo = models.CharField(max_length=100)

    class Meta:
        ordering = ('tipo',)
        verbose_name = 'Unidad del la Organizacion Social'
        verbose_name_plural = 'Unidades de los Organizaciones Sociales'

    def __str__(self):
        return self.tipo


class ComiteUnidadEjecutiva(models.Model):
    """!
    Clase que contiene el modelo de datos para Los Comites de la unidad ejecutiva

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-05-2017
    @version 1.0.0
    """
    fk_unidad = models.ForeignKey(UnidadesOrganizacionSocial, verbose_name="Unidad Ejecutiva")
    tipo = models.CharField(max_length=100)

    class Meta:
        ordering = ('tipo',)
        verbose_name = 'Comite de la Organizacion Social'
        verbose_name_plural = 'Comites de las Organizaciones Sociales'

    def __str__(self):
        return self.tipo


class TipoOrganizacion(models.Model):
    """!
    Clase que contiene el modelo de datos Para los tipos de organizaciones

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 20-07-2017
    @version 1.0.0
    """
    tipo = models.CharField(max_length=100, unique=True)
    abreviatura = models.CharField(max_length=4, unique=True)
    descripcion = models.TextField()

    class Meta:
        ordering = ('tipo',)
        verbose_name = 'Tipo de Organizacion'
        verbose_name_plural = 'Tipos de Organizaciones'

    def __str__(self):
        return self.tipo

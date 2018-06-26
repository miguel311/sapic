from __future__ import unicode_literals
"""
SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.modelsExplicacion.modelsExplicacionesSituacional
#
# Modelos correspondientes a la aplicación consulta
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

from django.contrib.gis.db import models

from explicacion_situacional.modelsEncuestas.modelsConsultas import Consulta

from organizaciones.models import OrganizacionSocial


class ExplicacionSituacional(models.Model):
    """!
    Clase que gestiona los datos de la explicacion sitauacional

    @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 13-09-2017
    @version 1.0.0
    """
    def get_upload_to(self, filename):
        return "organizaciones_sociales/%s/%s" % (self.fk_organizacion, filename)

    # Llave foranea de la organizacion
    fk_organizacion = models.ForeignKey(OrganizacionSocial)

    # Area del consejo comunal
    coordenadas = models.PolygonField()

    # Archivo del mapa cartografico de la comunidad
    map_cartografico = models.FileField(upload_to=get_upload_to)

    # Fecha en que fue realizada la explicacion situacional
    fecha = models.DateTimeField(auto_now=True)


    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 13-07-2017
            @version 1.0.0
        """
        ordering = ('fk_organizacion',)
        verbose_name = 'Explicacion situacional'
        verbose_name_plural = 'Explicaciones Situacionales'

    def __str__(self):
        """!
            Funcion que muestra la informacion de las Explicaciones Situacionales
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 13-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de la explicacion situacional
        """
        return str(self.fk_organizacion)


class ExplicSitConsulta(models.Model):
    """!
    Clase que gestiona los datos de la explicacion sitauacional

    @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 13-09-2017
    @version 1.0.0
    """

    #Llave foranea de la consulta
    fk_consulta = models.ForeignKey(Consulta)
    #Llave forenea de la explicacion situacional
    fk_explicacion = models.ForeignKey(ExplicacionSituacional)
    #Fecha en que se asigno la consulta
    fecha = models.DateTimeField(auto_now=True)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 13-07-2017
            @version 1.0.0
        """
        ordering = ('fk_consulta',)
        verbose_name = 'Asignacion de Consulta a una explicacion situacional'
        verbose_name_plural = 'Asignaciones de consultas a las explicaciones situacionales'

    def __str__(self):
        """!
            Funcion que muestra la informacion de las Asignacion de la consulta a una explicacion situacional
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 13-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de la asignacion de la consulta a una explicacion situacional
        """
        return str(self.fk_consulta)

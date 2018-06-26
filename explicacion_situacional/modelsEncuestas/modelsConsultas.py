from __future__ import unicode_literals
"""
SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.modelsEncuestas.modelsConsultas
#
# Modelos correspondientes a la aplicación consulta
# @author Rodrigo Boet (rboet at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0


from django.db import models
from django.contrib.auth.models import User


class Caracterizacion(models.Model):
    """!
    Clase que gestiona los datos de la Caracterización sitauacional

    @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 18-09-2017
    @version 1.0.0
    """
    caracterizacion = models.CharField(unique=True, max_length=128,
                                 verbose_name='Caracterización')
    descripcion = models.TextField()

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 18-07-2017
            @version 1.0.0
        """
        ordering = ('caracterizacion',)
        verbose_name = 'Caracterización'
        verbose_name_plural = 'Características'

    def __str__(self):
        """!
            Funcion que muestra la informacion de las Características de la explicacion situacional
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 18-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de la asignacion de la Características de una explicacion situacional
        """
        return self.caracterizacion


class Consulta(models.Model):
    """!
    Clase que gestiona los datos de la consulta

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 15-02-2017
    @version 1.0.0
    """
    #Agregado Caracterización by Leonel Hernandez 
    fk_caracterizacion = models.ForeignKey(Caracterizacion)

    ## Nombre de la consulta
    nombre_consulta = models.CharField(max_length=128, unique=True)

    ## Estado de la consulta
    activa = models.BooleanField(default=True)

    ## Relación con el user
    user = models.ForeignKey(User)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 18-07-2017
            @version 1.0.0
        """
        ordering = ('nombre_consulta',)
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        """!
            Funcion que muestra la informacion de las Consultas de la explicacion situacional
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 18-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de la asignacion de la Consulta de una explicacion situacional
        """
        return self.nombre_consulta


class TipoPregunta(models.Model):
    """!
    Clase que gestiona los tipos de preguntas

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 15-02-2017
    @version 1.0.0
    """
    ## Nombre de la consulta
    tipo = models.CharField(max_length=30)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 13-07-2017
            @version 1.0.0
        """
        ordering = ('tipo',)
        verbose_name = 'Tipo Pregunta'
        verbose_name_plural = 'Tipos de Preguntas'

    def __str__(self):
        """!
            Funcion que muestra la informacion de los tipos de preguntas
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 13-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos del tipo de pregunta
        """
        return self.tipo


class Pregunta(models.Model):
    """!
    Clase que gestiona los datos de la pregunta

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 15-02-2017
    @version 1.0.0
    """
    ## Texto de la pregunta
    texto_pregunta = models.TextField()

    ## Relación con el tipo de pregunta
    tipo_pregunta = models.ForeignKey(TipoPregunta)

    ## Relación con la consulta
    consulta = models.ForeignKey(Consulta)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 18-07-2017
            @version 1.0.0
        """
        ordering = ('consulta',)
        verbose_name = 'pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        """!
            Funcion que muestra la informacion de las Preguntas de la explicacion situacional
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 18-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de la asignacion de la Pregunta de una explicacion situacional
        """
        return self.texto_pregunta

class Opcion(models.Model):
    """!
    Clase que gestiona las opciones de las preguntas

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 15-02-2017
    @version 1.0.0
    """
    ## Texto de la opción
    texto_opcion = models.TextField()

    ## Relación con la pregunta
    pregunta = models.ForeignKey(Pregunta)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 18-07-2017
            @version 1.0.0
        """
        ordering = ('pregunta',)
        verbose_name = 'Opcion'
        verbose_name_plural = 'Opciones'

    def __str__(self):
        """!
            Funcion que muestra la informacion de las Opciones a la pregunta
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 18-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos la opcion a la pregunta
        """
        return self.texto_opcion

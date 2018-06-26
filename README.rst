Para instalar la apliacacion en modo desarrollo debera seguir los siguientes pasos:

1-) Instalar el controlador de versiones git:
    
    $ su

    # aptitude install git

2-) Descargar el codigo fuente del proyecto SAPIC:

    Para descargar el código fuente del proyecto contenido en su repositorio GIT realice un clon del proyecto SAPIC, como el certificado digital del servidor está autofirmado entonces debemos saltar su chequeo con el siguiente comando:

    $ export GIT_SSL_NO_VERIFY=True

    $ https://planificacion.cenditel.gob.ve/scm/git/sapic.git

3-) Crear un Ambiente Virtual:

    El proyecto está desarrollado con el lenguaje de programación Python, se debe instalar Python v3.4.2. Con los siguientes comandos puede instalar Python y PIP.

    Entrar como root para la instalacion 

    # aptitude install python3.4 python3-pip python3.4-dev python3-setuptools

    # aptitude install python3-virtualenv virtualenvwrapper

    Salir del modo root y crear el ambiente:

    $ mkvirtualenv --python=/usr/bin/python3 sapic

4-) Instalar los requerimientos del proyecto 

    Para activar el ambiente virtual SAPIC ejecute el siguiente comando:

    $ workon sapic
    (sapic)$

    Entrar en la carpeta raiz del proyecto:

    (sapic)$ cd sapic
    (sapic)sapic$ 

    Desde ahi se deben instalar los requirimientos del proyecto con el siguiente comando:

    (sapic)$ pip install -r requerimientos.txt

    De esta manera se instalaran todos los requerimientos iniciales para montar el proyecto 
    
    Nota: Si hay problemas en la instalación del paquete lxml==3.6.0 descrito en el fichero requirements.txt es
    necesario instalar los siguientes paquetes como usuario root:

    # apt-get install python3-lxml
    
    # apt-get install libxml2-dev libxslt-dev python-dev

    # apt-get build-dep python3-lxml

    Luego ejecutamos de nuevo el siguiente comando:

    (sapic)$ pip install -r requerimientos.txt

5-) Crear base de datos y Migrar los modelos:

    El manejador de base de datos que usa el proyecto es postgres, es necesario, tener instalado postgres y crear la base de datos desde postgres de la siguiente manera si se usa la consola de postgres, ademas se debe instalar postgis para el uso de una base de datos georeferenciada:

    como super usuario instalar postgis
    # aptitude install postgis
    # aptitude install postgresql-x.x-postgis-x.x


    postgres=# CREATE DATABASE sapic OWNER=postgres ENCODING='UTF−8';
    postgres=# \q
    $ psql sapic
    sapic=# CREATE EXTENSION postgis;

    Para migrar los modelos del proyecto se debe usar el siguiente comando:

    (sapic)$ python manage.py makemigrations
    (sapic)$ python manage.py migrate

6-) Cargar data inicial del proyecto 

    Asegurese de que los modelos esten migrados en base de datos y ejecute los siguientes comando para cargar la data inicial del proyecto:

    Esto permitira cargar los grupos de usuarios y permisos de los usuarios y el superusuario:
    (sapic)$ python manage.py loaddata fixtures/initial_data_auth.json

    Esto permitira cargar los datos de los estados, municipios, parroquias y utilidades de la aplicacion:
    (sapic)$ python manage.py loaddata fixtures/initial_data_utils.json
    
    Esto permitira cargar los datos iniciales del usuario admin de la aplicacion:
    (sapic)$ python manage.py loaddata fixtures/initial_data_users.json

    Esto permitira cargar los datos iniciales de las preguntas de las consulta relacionadas a la explicacion situacional:
    (sapic)$ python manage.py loaddata fixtures/initial_tipo_pregunta.json

    Esto permitira cargar los datos iniciales de las caracteristicas de las consulta relacionadas a la explicacion situacional:
    (sapic)$ python manage.py loaddata fixtures/initial_data_caracterizacion.json

    Esto permitira cargar los datos iniciales de las consultas relacionadas a la explicacion situacional:
    (sapic)$ python manage.py loaddata fixtures/initial_data_consultas.json

    Esto permitira cargar los datos iniciales de las preguntas relacionadas a las consultas de la explicacion situacional:
    (sapic)$ python manage.py loaddata fixtures/initial_data_preguntas.json

    Esto permitira cargar los datos iniciales de las opciones de seleccion simple o multiples relacionadas a las preguntas de las consultas:
    (sapic)$ python manage.py loaddata fixtures/initial_data_opciones.json

7-) Correr la aplicacion SAPIC

    Para correr la apliacion se debe  ejecutar el siguiente comando:

    (sapic)$ python manage.py runserver

    Ingresar a la plataforma con la siguientes credenciales:

    Username: admin

    password: 1234567890administrador
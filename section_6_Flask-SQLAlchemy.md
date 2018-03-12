# Flask SQLAlchemy

## Índice

* [Installaciones necesarias](#installaciones-necesarias)

## Installaciones necesarias

* Crear el entorno virtiual: ```virtualenv --python "C:\Users\Gabriel\AppData\Local\Programs\Python\Python36-32\python.exe" venv```
* Activar al entorno virtual: ```.\venv\Scripts\activate.bat```
* Instalar Flask en el entorno virtual: ```pip install Flask```
* Instalar Flask-JWT en el entorno virtual: ```pip install Flask-JWT```
* Instalar Flask-RESTful en el entorno virtual: ```pip install Flask-RESTful```
* Instalar Flask-SQLAlchemy en el entorno virtual: ```pip install Flask-SQLAlchemy```

```
(venv) C:\Users\montoya\Desktop\CursoRestAPIFlask\section_06_Flask_SQLAlchemy>pip freeze
aniso8601==3.0.0
click==6.7
Flask==0.12.2
Flask-JWT==0.3.2
Flask-RESTful==0.3.6
Flask-SQLAlchemy==2.3.2
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
PyJWT==1.4.2
pytz==2018.3
six==1.11.0
SQLAlchemy==1.2.5
Werkzeug==0.14.1

(venv) C:\Users\montoya\Desktop\CursoRestAPIFlask\section_06_Flask_SQLAlchemy>
```

## organizar el proyecto en packages

* Crear la carpeta del paquete: ``models`` y ``resources``
* Dentro de cada carpeta que va a ser definida como paquete se debe crear el archivo ``__init__.py``

 
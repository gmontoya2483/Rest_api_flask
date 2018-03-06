# Section 3: Your first REST API

## Instalacion de Flask

Ejecutar el siguiente comando: ```pip install flask``` ó ```pip3 install flask```, si se tienen en la computadora las 2 versiones de python.

Este comando va a instalar las siguientes librerias:

```
    Microsoft Windows [Version 6.1.7601]
    Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

    C:\WINDOWS\system32>pip install flask
    Collecting flask
    Downloading Flask-0.12.2-py2.py3-none-any.whl (83kB)
        100% |████████████████████████████████| 92kB 449kB/s
    Collecting click>=2.0 (from flask)
    Downloading click-6.7-py2.py3-none-any.whl (71kB)
        100% |████████████████████████████████| 71kB 1.6MB/s
    Collecting itsdangerous>=0.21 (from flask)
    Downloading itsdangerous-0.24.tar.gz (46kB)
        100% |████████████████████████████████| 51kB 1.0MB/s
    Collecting Werkzeug>=0.7 (from flask)
    Downloading Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
        100% |████████████████████████████████| 327kB 1.1MB/s
    Collecting Jinja2>=2.4 (from flask)
    Downloading Jinja2-2.10-py2.py3-none-any.whl (126kB)
        100% |████████████████████████████████| 133kB 2.0MB/s
    Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->flask)
    Downloading MarkupSafe-1.0.tar.gz
    Installing collected packages: click, itsdangerous, Werkzeug, MarkupSafe, Jinja2, flask
    Running setup.py install for itsdangerous ... done
    Running setup.py install for MarkupSafe ... done
    Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 flask-0.12.2 itsdangerous-0.24
```

[Video: Explicacion sobre instalación de Flask](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960108?start=0)

## Flask app structure and how to run it

```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello, world!!"

    app.run(port=5000)
```

Guardar el archivo en este caso con el nombre ```app.py```

Para ejecutar ```python app.py```

```
    C:\Users\montoya\Desktop\CursoRestAPIFlask\section_03_your_first_rest_api>python app.py
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

[Video: Primera applicacion Flask](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960110?start=0)
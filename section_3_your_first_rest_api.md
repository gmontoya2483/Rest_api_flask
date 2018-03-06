# Section 3: Your first REST API

## Instalación de Flask

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

## First Flask application, structure and how to run it

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

## Creando los Endpoits

```python
    from flask import Flask

    app = Flask(__name__)

    stores = [
        {
            'name':'My Onderful Store',
            'items': [
                {
                    'name': 'My Item',
                    'price': 15.99
                }
            ]
        }
    ]

    # POST - used to receive data
    # GET - used to send data back only

    # POST /store data: {name:}
    @app.route('/store', methods=['POST'])
    def create_store():
        pass

    # GET /store/<string:name>
    @app.route('store/<string:name>', methods=['GET'])
    def get_store (name):
        pass

    # GET /store
    @app.route('store', methods=['GET'])
    def get_stores ():
        pass

    # POST /store/<string:name>/item {name:, price:}
    @app.route('/store/<string:name>/item', methods=['POST'])
    def create_item_in_store(name):
        pass

    # GET /store/<string:name>/item
    @app.route('store/<string:name>/item', methods=['GET'])
    def get_item_in_store (name):
        pass


    app.run(port=5000)
```

[Video: Creando los endpoints en Flask](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960116?start=0)

## Implementar un GET simple sin argumentos

Primero se debe importar el metodo ```jsonify``` del paquete flask

```python
    from flask import Flask, jsonify
```

```python
    # GET /store
    @app.route('/store', methods=['GET'])
    def get_stores ():
        return jsonify({'stores':stores})
```

> ```jsonify``` toma como argumento un diccionario

despues de llamar ```http://127.0.0.1:5000/store``` en un web browser obtenemos el siguiente resultado:  

```json
    {
        "stores": [
            {
            "items": [
                {
                "name": "My Item", 
                "price": 15.99
                }
            ], 
            "name": "My Onderful Store"
            }
        ]
    }
```

[Video: Recibir una lista de stores ](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960118?start=0)


## Implementar el resto de los endpoints

### implementar un simple POST

Primero se debe importar el metodo ```request``` del paquete flask

```python
    from flask import Flask, jsonify, request
```

```python
    # POST /store data: {name:}
    @app.route('/store', methods=['POST'])
    def create_store():
        request_data = request.get_json()
        new_store = {
            'name': request_data['name'],
            'items': []
        }
        stores.append(new_store)
        return jsonify(new_store)
```



### implementar un GET de un store específico

```python
    # GET /store/<string:name>
    @app.route('/store/<string:name>', methods=['GET'])
    def get_store (name):
        for store in stores:
            if store['name'] == name:
                return jsonify(store)

        return jsonify ({'message':'store not found'})
```

Despues de llamar ```http://127.0.0.1:5000/store/nombre inexistente``` en un web browser obtenemos el siguiente resultado:

```json
    {
        "message": "store not found"
    }
```

Despues de llamar ```http://127.0.0.1:5000/store/My%20Onderful%20Store``` en un web browser obtenemos el siguiente resultado:

```json
    {
    "items": [
        {
        "name": "My Item", 
        "price": 15.99
        }
    ],
    "name": "My Onderful Store"
    }
```

### implementar un GET para obtener todos los items de un store

```python
    # GET /store/<string:name>/item
    @app.route('/store/<string:name>/item', methods=['GET'])
    def get_item_in_store (name):
        for store in stores:
            if store['name'] == name:
                return jsonify({'items':store['items']})

        return jsonify ({'message':'store not found'})
```

Despues de llamar ```http://127.0.0.1:5000/store/nombre inexistente/item``` en un web browser obtenemos el siguiente resultado:

```json
    {
        "message": "store not found"
    }
```

Despues de llamar ```http://127.0.0.1:5000/store/My%20Onderful%20Store/item``` en un web browser obtenemos el siguiente resultado:

```json
    {
    "items": [
        {
        "name": "My Item", 
        "price": 15.99
        }
    ]
    }
```

### implementar un POST para agregar items a un store

```python
    # POST /store/<string:name>/item {name:, price:}
    @app.route('/store/<string:name>/item', methods=['POST'])
    def create_item_in_store(name):
        request_data = request.get_json()
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }

        for store in stores:
            if store['name'] == name:
                store['items'].append(new_item)
                return jsonify(new_item)

        return jsonify ({'message':'store not found'})
```

[Video: Implementar el resto de los endpoints ](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960120?start=0)
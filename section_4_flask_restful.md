# Flask-RESTful

## Crear un entorno virtual

Un entorno virtual nos da una instalacion limpia de Python. Esto nos permite hacer que los proyectos no compartan librerias. Podemos tener dos o mas proyectos corriendo la misma libreria pero diferentes versiones.

> Para saber que librerias tenemos instaladas y las versiones, ejecutar el siguiente comando: ```pip freeze```

1. Instalar la herramienta ```virtualenv``` ejecutando el siguiente comando:

    ```pip install virtualenv```

2. Crear el entorno virtual ejecuanto el siguiente comando dentro de la carpeta donde queremos crearlo:

    ```virtualenv --python "C:\Users\Gabriel\AppData\Local\Programs\Python\Python36-32\python.exe" venv```

    Output:

    ```
    Using base prefix 'C:\\Users\\Gabriel\\AppData\\Local\\Programs\\Python\\Python36-32'
    New python executable in C:\Users\Gabriel\Documents\Projects\curso_rest_api_flask\section_04_Flask_Restful\venv\Scripts\python.exe
    Installing setuptools, pip, wheel...done.
    Running virtualenv with interpreter C:\Users\Gabriel\AppData\Local\Programs\Python\Python36-32\python.exe
    ```
    > Estas instrucciones son validas solo para Windows10, para otros entornos Mac, Linux ver las referencias en el video.

    Este comando nos crea una carpeta llamada venv dentro del directorio donde nos encontramos.

3. Activar el entorno virtual ejecutando el siguiente comando:  

    ```.\venv\Scripts\activate.bat```

    > Estas instrucciones son validas solo para Windows10, para otros entornos Mac, Linux ver las referencias en el video.

4. Para salir del entorno virtual ejecuar el siguiente comando: ```deactivate```

## Instalar la libreria Flask-Restful

Para instalar esta libreria ejecutar el comando ```pip install Flask-RESTful```. Al instalar esta libreria tambien instsala la libreria de Flask.

```
(venv) pip freeze
    click==6.7
    Flask==0.12.2
    itsdangerous==0.24
    Jinja2==2.10
    MarkupSafe==1.0
    SQLAlchemy==1.2.2
    virtualenv==15.1.0
    Werkzeug==0.14.1
```

>Nota: Si estamos dentro del entorno virtual la libreria va a ser cargada solo para el entorno virtual. Por otro lado si estamos fuera del entorno virtual esta libreria no va a ser accesible por el mismo.

[Video: Virtualenvs and setting up Flask-RESTful](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960148?start=0)

## Primera aplicacion Flask-RESTful

> Crear la carpeta donde se va a alojar el código desde la consola estando dentro del entorno virtual. Crear dentro de esta carpeta el archivo ```app.py```.

Importar las clases ```Resource``` y ```Api``` del modulo ```flask_restful```. Además importar la clase ```Flask``` del modulo ```flask```

```python
    from flask import Flask
    from flask_restful import Resource, Api
```

* RESTful api basica con un recurso y meodo ```GET```:  

```python
    from flask import Flask
    from flask_restful import Resource, Api

    app = Flask (__name__)
    api = Api(app)

    class Student(Resource):
        def get (self, name):
            return {'student':name}

    api.add_resource(Student, '/student/<string:name>')

    app.run(port=5000)
```

* Ejecutar el archivo ```app.py``` desde el entorno virtual:  

    ```python app.py```

[Video: primera aplicacion Flask-RESTful](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960152?start=0)

## Crear el recurso Item

```python
    items = []

    class Item(Resource):
    def get (self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    api.add_resource(Item, '/item/<string:name>')
```

> **html codes:**  
> 200 OK  
> 201 CREATED  
> 202 ACCEPTED  
> 404 NOT FOUND  

[Video: Crear el recurso Item](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960156?start=0)

## Crear el recurso para Items

```python
    class ItemList(Resource):
    def get (self):
        return {'items': items}

    api.add_resource(ItemList, '/items')
```

[Video: Crear el recurso Items](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960160?start=0)

## Mejoras en el Recurso Item

```python
    class Item(Resource):
        def get (self, name):
            item = next(filter(lambda item: item['name'] == name, items), None)
            return {'item': item}, 200 if item is not None else 404

        def post(self, name):
            if next(filter(lambda item: item['name'] == name, items), None) is not None:
                return {'message': "An item with name '{}' already exist".format(name)}, 400

            data = request.get_json()
            item = {'name': name, 'price': data['price']}
            items.append(item)
            return item, 201

    api.add_resource(Item, '/item/<string:name>')
```

> Con esta mejora se reemplaza el loop para buscar el item con un filtro, además antes de insertar el nuevo item se verifica que no exista.

> **html codes:**  
> 200 OK  
> 201 CREATED  
> 202 ACCEPTED  
> 404 NOT FOUND 
> 400 BAD REQUEST  

[Video: Mejora de codigo y control de errores](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960162?start=0)

## Authentication and Logging in

1. Instalar la libreria ```Flask JWK``` ejecutando el siguiente comando dentro del entorno virtual:  

    ```pip install Flask-JWT```

    > **JWT:** Json Web Token

2. Crear la ```Secret Key``` de la aplicacion dentro del archivo ```app.py```  
    ```python
        app = Flask (__name__)
        api = Api(app)

        app.secret_key = 'my_secret_key'
    ```

3. Crear el archivo ```user.py``` dentro de la carpeta ```code```  

    ```python
        class User:
            def __init__(self, _id, username, password):
                self.id = _id
                self.username = username
                self.password = password
    ```

4. Crear el archivo ```security.py``` dentro de la carpeta ```code```  

    ```python
        from user import User
        from werkzeug.security import safe_str_cmp

        users = [
            User(1, 'bob', 'asdf')
        ]

        username_mapping = {user.username: user for user in users}

        userid_mapping = {user.id: user for user in users}


        def authenticate(username, password):
            user = username_mapping.get(username, None)
            if user and safe_str_cmp(user.password, password):
                return user


        def identity(payload):
            user_id = payload['identity']
            return userid_mapping.get(user_id, None)

    ```

5. Configurar **JWT** para trabajar con nuestra aplicacion  

    * Se tiene que importar las siguientes librerias dentro del archivo ```app.py```: 

        ```python
            from flask_jwt import JWT, jwt_requiered
        ```

    * Se tiene que importar también del archivo ```security.py``` las funciones ```authenticate``` e ```identity```  

        ```python
            from security import authenticate, identity
        ``` 

    * Se debe crear una variable del tipo ```JWT```  

        ```python
            jwt = JWT(app, authenticate, identity)
        ```

        > ```JWT``` crea un nuevo endpoint `/auth` que cuando es llamado se debe enviar el **username** y el **password**. Este Endpoint devuelve un **JWT token** que es utilizado en los proximos requests.

    * Para determinar que metodo necesita authenticacion para ser ejecutado se debe colocoar el **decorador** ```@jwt_requiered()```

        ```python
            @jwt_required()
            def get (self, name):              
                item = next(filter(lambda item: item['name'] == name, items), None)
                return {'item': item}, 200 if item is not None else 404
        ```

6. Utilizar el **JWT** token

* Llamar al Endpoint ```/auth```

    >**Header**  
    >Key: Content-Type, Value: application/json  
    >  
    >**Body**  
    >{"username": "bob", "password": "asdf"}

    Es llamado nos devulve un **access_token**

    ```json
    {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjA0MzI1ODYsImlhdCI6MTUyMDQzMjI4NiwibmJmIjoxNTIwNDMyMjg2LCJpZGVudGl0eSI6MX0.VHBc12FJ63T_7jyeRhKjIRO8ysNgRx9aIPhsfEf0vzg"
    }
    ```
* Llamar un Endpoint utilizando el Token

    >**Header**  
    >Key: Authorization, Value: JWT _+ Token_  

[Video: Authentication and loggin in - Parte 1](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960168?start=0)  
[Video: Authentication and loggin in - Parte 2](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960170?start=0)

## Metodo para borrar un recurso Item

```python
    def delete(self, name):
    global items
    items = list(filter(lambda item: item['name'] != name, items))
```
[Video: Crear un metodo PUT](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960174?start=0)

## Metodo PUT para modificar o insertar un recurso Item

```python
    def put (self, name):
        data = request.get_json()
        item = next(filter(lambda item: item['name'] == name, items), None)

        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
```

[Video: Crear un metodo PUT](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960178?start=0)

## Request parsing

* Importar ```reqparse``` de la libreria ```flask_restful```  

    ```python
        from flask_restful import Resource, Api, reqparse
    ```

* Agregar al parse a la funcion que recibe el JSON

    ```python
        def put (self, name):

            parser = reqparse.RequestParser()
            parser.add_argument('price',
                type = float,
                required = True,
                help = "This field cannot be left blank!!"
            )
            data = parser.parse_args()

            item = next(filter(lambda item: item['name'] == name, items), None)

            if item is None:
                item = {'name': name, 'price': data['price']}
                items.append(item)
            else:
                item.update(data)
            return item
    ```

    > Si el request tiene otros atributos además del price, los va a descartar.  
    > En caso que no se envie el argumento ```price```, se va a devolver el siguiente mensaje:  
    > ```json
    >{
    >   "message": {
    >       "price": "This field cannot be left blank!!"
    >   }
    >}
    > ```  

    [Video: Parse the request](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960180?start=0)
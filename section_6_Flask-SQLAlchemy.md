# Flask SQLAlchemy

## Índice

* [Installaciones necesarias](#installaciones-necesarias)
* [Organizar el proyecto en packages](#organizar-el-proyecto-en-packages)
* [## Creando los modelos y recursos de User y Item](#creando-los-modelos-y-recursos-de-User-y-Item)


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

## Organizar el proyecto en packages

* Crear la carpeta del paquete: ``models`` y ``resources``
* Dentro de cada carpeta que va a ser definida como paquete se debe crear el archivo ``__init__.py``

[Video: Mejorando la estructura del proyecto](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/6020490?start=0)

## Creando los modelos y recursos de User y Item

* User Model

```python
import sqlite3

class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()

        if row is not None:
            user = cls(*row)  # *row = row[0], row[1], row[2]
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row is not None:
            user = cls(*row)  # *row = row[0], row[1], row[2]
        else:
            user = None

        connection.close()
        return user
```

* Item Model

```python
import sqlite3

class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(row[0], row[1])

    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query,(self.name, self.price,))

        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query,(self.price, self.name,))

        connection.commit()
        connection.close()
```

* Recurso User

```python
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type = str,
            required = True,
            help = "This field cannot be left blank!!"
    )

    parser.add_argument('password',
            type = str,
            required = True,
            help = "This field cannot be left blank!!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "An user with name '{}' already exist".format(data['username'])}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password'],))

        connection.commit()
        connection.close()

        return {"message": "User created"}, 201
```

* Recurso Item

```python
import sqlite3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type = float,
            required = True,
            help = "This field cannot be left blank!!"
    )

    @jwt_required()
    def get (self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exist".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])
        try:
            item.insert()
        except:
            return {'message': "An error occurred inserting the item."},500

        return item.json(), 201


    def delete(self, name):
        if ItemModel.find_by_name(name) is None:
            return {'message': "An item with name '{}' does not exist".format(name)}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query,(name,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

    def put (self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                updated_item.insert()
            except:
                return {'message': "An error occurred inserting the item."},500
            return updated_item.json(), 201
        else:
            try:
                updated_item.update()
            except:
                return {'message': "An error occurred updating the item."},500
            return updated_item.json()


class ItemList(Resource):

    def get (self):
        list_of_items=[]

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from items"
        result = cursor.execute(query)

        for row in result:
            item = {'name': row[0], 'price':row[1]}
            list_of_items.append(item)

        connection.close()
        return {'items':list_of_items}
```

[Video: Creando los modelos](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/6020492?start=0)


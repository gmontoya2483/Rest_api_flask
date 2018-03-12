# Flask SQLAlchemy

[VOLVER A README.md](README.md)

## Índice

* [Installaciones necesarias](#installaciones-necesarias)
* [Organizar el proyecto en packages](#organizar-el-proyecto-en-packages)
* [Creando los modelos y recursos de User y Item](#creando-los-modelos-y-recursos-de-User-y-Item)
* [Configurando SQLAlchemy](configurando-sqlalchemy)
* [Implementar el ItemModel usando Flask-SQLAlchemy](#implementar-el-itemmodel-usando-flask-sqlalchemy)
* [Implementar el UserModel usando Flask-SQLAlchemy](#implementar-el-usermodel-usando-flask-sqlalchemy)
* [Mostrar todos los items](mostrar-todos-los-items)

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

## Configurando SQLAlchemy

* Crear el archivo ``db.py``, que va a estar en cargado de hostear el objeto SQLAlchemy.

    ```python
        from flask_sqlalchemy import SQLAlchemy

        db = SQLAlchemy()
    ```

* Importar el objeto SQLAlchemy dentro del ``app.py`` e inicializar la app.

    ```python
        if __name__ == '__main__':
            from db import db
            db.init_app(app)
            app.run(port=5000, debug=True)
    ```

* Hacer que los Modelos extiendas de ``db.Model``, asignar el table name y el mapeo de las columnas.

    ```python
        import sqlite3
        from db import db

        class ItemModel(db.Model):

            __tablename__ = 'items'

            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(80))
            price = db.Column(db.Float(precision=2))

            ...
    ```

    ```python
    import sqlite3
    from db import db

    class UserModel(db.Model):

        __tablename__ = 'users'

        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80))
        password = db.Column(db.String(80))

        ...

    ```

* Definir las propiedades de configuracion de ``Flask-SQLALchemy``.

```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

[Video: configurando SQLAlchemy](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/6020504?start=0)

## Implementar el ItemModel usando Flask-SQLAlchemy

* Item Model

```python
import sqlite3
from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
```

* Item Resource

```python
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
            item.save_to_db()
        except:
            return {'message': "An error occurred inserting the item."},500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put (self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json()
```

[Video: Implementar el ItemModel usando Flask-SQLAlchemy](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/6020506?start=0)

## Implementar el UserModel usando Flask-SQLAlchemy

* User Model

    ```python
        import sqlite3
        from db import db

        class UserModel(db.Model):

            __tablename__ = 'users'

            id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String(80))
            password = db.Column(db.String(80))

            def __init__(self, username, password):
                self.username = username
                self.password = password

            @classmethod
            def find_by_username(cls, username):
                return cls.query.filter_by(username=username).first()

            @classmethod
            def find_by_id(cls, _id):
                return cls.query.filter_by(id=_id).first()

            def save_to_db(self):
                db.session.add(self)
                db.session.commit()
    ```

* User Resource

    ```python
        import sqlite3
        from flask_restful import Resource, reqparse
        from models.user import UserModel

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

                user = UserModel(data['username'], data['password'])
                user.save_to_db()

                return {"message": "User created"}, 201
    ```

[Video: implementar el UserModel](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/6020508?start=0)

## Mostrar todos los items

* Modificar el resource item

```python
    class ItemList(Resource):

    def get (self):
        return {'items': [item.json() for item in ItemModel.query.all()]}

```

[Video: Mostrar todos los items](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/6020510?start=0)
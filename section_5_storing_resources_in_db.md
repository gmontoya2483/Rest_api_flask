# Storing Resources in an SQL Database

## Índice

* [Comandos basicos de SQL](#comandos_basicos_de_sql) 

## Comandos basicos de SQL

```python
    import sqlite3

    connection = sqlite3.connect('data.db')

    cursor = connection.cursor()

    create_table = "CREATE TABLE users (id int, username text, password text)"

    cursor.execute(create_table)

    user = (1, 'jose', 'asdf')
    insert_query = "INSERT INTO users VALUES (?, ?, ?)"
    cursor.execute(insert_query, user)


    users = [(2, 'rolf', 'asdf'), (3, 'anne', 'asdf')]
    cursor.executemany(insert_query,users)


    select_query = "SELECT * FROM users"
    for row in cursor.execute(select_query):
        print(row)


    connection.commit()
    connection.close()
```

[Video: Comandos basicos de SQL](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5965476?start=0)

## Logging in and retrieving Users from database

1. Modificar ```user.py``` para agregar 2 metodos de clases que busquen en la base de datos el usuario por ```username``` y por ```_id```

    ```python
        import sqlite3
    ```

    ```python
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
    ```

    ```python
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

2. Modificar ```security.py``` para utilizar los m'etodos de la clase User

```python
    from user import User
    from werkzeug.security import safe_str_cmp

    def authenticate(username, password):
        user = User.find_by_username(username)
        if user and safe_str_cmp(user.password, password):
            return user


    def identity(payload):
        user_id = payload['identity']
        return User.find_by_id(user_id)
```

[Video: Logging in](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5965500?start=0)
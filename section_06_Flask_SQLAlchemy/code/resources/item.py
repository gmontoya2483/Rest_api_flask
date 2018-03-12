import sqlite3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required


items = []

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type = float,
            required = True,
            help = "This field cannot be left blank!!"
    )

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item':{'name':row[0], 'price': row[1]}}

    @classmethod
    def insert_item(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query,(item['name'], item['price'],))

        connection.commit()
        connection.close()

    @classmethod
    def update_item(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query,(item['price'], item['name'],))

        connection.commit()
        connection.close()



    @jwt_required()
    def get (self, name):
        item = Item.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404


    def post(self, name):
        if Item.find_by_name(name):
            return {'message': "An item with name '{}' already exist".format(name)}, 400
        
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        try:
            Item.insert_item(item)
        except:
            return {'message': "An error occurred inserting the item."},500

        return item, 201


    def delete(self, name):
        if Item.find_by_name(name) is None:
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
        item = Item.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}

        if item is None:
            try:
                Item.insert_item(updated_item)
            except:
                return {'message': "An error occurred inserting the item."},500
            return updated_item, 201
        else:
            try:
                Item.update_item(updated_item)
            except:
                return {'message': "An error occurred updating the item."},500
            return updated_item

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


    
        
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask (__name__)
api = Api(app)
app.secret_key = 'my_secret_key'

jwt = JWT(app, authenticate, identity)



items = []

class Item(Resource):
    
    @jwt_required()
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

    def delete(self, name):
        global items
        items = list(filter(lambda item: item['name'] != name, items))
        return {'message': 'Item deleted'}
    
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

api.add_resource(Item, '/item/<string:name>')


class ItemList(Resource):
    def get (self):
        return {'items': items}

api.add_resource(ItemList, '/items')


app.run(port=5000, debug=True)

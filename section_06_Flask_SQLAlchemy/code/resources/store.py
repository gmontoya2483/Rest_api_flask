from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from models.store import StoreModel

class Store(Resource):
    def get (self, name):
        store= StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message': 'Store {} not found'.format(name)}, 404 
    
    def post (self, name):
        store= StoreModel.find_by_name(name)
        if store:
            return {'message': 'A store with name {}, already exists'.format(name)}, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurrd while creating the store'},500
        
        return store.json(),201

    
    def delete (self, name):
        store= StoreModel.find_by_name(name)
        if store is None:
            return {'message': 'A store with name {}, does not exists'.format(name)}, 400
        
        try:
            store.delete_from_db()
        except:
            return {'message': 'An error occurrd while deleting the store'},500
        
        return {'message': 'Store {} deleted'.format(name)}

class StoreList(Resource):
    def get (self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}



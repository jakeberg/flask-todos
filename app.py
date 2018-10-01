

from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class ItemResource(Resource):
    def get(self, id):
         return {'message': 'Get an item id: %s' % (id)}

    def put(self, id):
        data = request.get_json()
        name = data.get('name', None)
        return {'message': 'Update an item id: %s, name: %s' % (id, name)}

    def delete(self, id):
        return {'message': 'Delete an item id: %s' % (id)}

class ItemListResource(Resource):

    def get(self):
        return {'message': 'Get a list of items'}

    def post(self):
        data = request.get_json()
        name = data.get('name', None)
        return {'message': 'Create an item with name: %s' % (name)}

api.add_resource(ItemResource, '/item/<id>')
api.add_resource(ItemListResource, '/items')

if __name__ == '__main__':
     app.run(debug=True)


from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

from datetime import datetime, date
todos = {

    1: {'title': 'do something',
        'creation_date': '',
        'last_updated_date': ''},
    2: {'title': 'more stuff',
        'creation_date': '',
        'last_updated_date': ''},
}

class TodoResource(Resource):
    def get(self, todo_id):
        timestamp = datetime.now()
        return {'message': 'Get an item id: %s' % (todo_id)}

    def put(self, todo_id):
        data = request.get_json()
        timestamp = datetime.now()
        name = data.get('name', None)
        return {'message': 'Update an item id: %s, name: %s' % (id, name)}

    def delete(self, todo_id):
        return {'message': 'Delete an item id: %s' % (id)}

api.add_resource(TodoResource, '/todo/<todo_id>')

if __name__ == '__main__':
     app.run(debug=True)


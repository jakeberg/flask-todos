from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

from datetime import datetime, date
import json
import logging

# Builds custom logger
LOGFILE = "./todos.log"
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(filename)s : %(message)s')
r_logger = RotatingFileHandler(LOGFILE, mode='a', maxBytes=5*1024*1024, 
                                 backupCount=2, encoding=None, delay=0)
r_logger.setFormatter(formatter)
logger.addHandler(r_logger)
logger.setLevel(logging.INFO)

todos = {

    1: {
        "title":"do somethin",
        "creation_date": "2018-10-02 15:07:08.183240",
        "last_updated_date": "2018-10-02 15:07:08.183240",
        "due_date": "12-2-2018",
        "completed": False,
        "completion_date": "incomplete"
    },

    2: {
        "title":"todo number 2",
        "creation_date": "2018-10-02 15:07:08.183240",
        "last_updated_date": "2018-10-02 15:07:08.183240",
        "due_date": "1-2-2019",
        "completed": False,
        "completion_date": "incomplete"
    },
}

class TodoListResource(Resource):

    def get(self):
        logger.info("User ")
        try:
            logger.info("User accessed all todos")
            return todos
        except:
            logger.error("User accessed all todos")
            return "Something happened and request was not made..."


    def post(self):
        data = request.get_json()
        timestamp = datetime.now()
        
        new_todo = {
            "title": data["title"],
            "creation_date": str(timestamp),
            "last_updated_date": str(timestamp),
            "due_date": data["due_date"],
            "completed": data["completed"],
            "completion_date": "incomplete"
            }
        new_index = len(todos) + 1
        todos[new_index] = new_todo

        name = todos.get("title", data["title"])
        return {'message': 'Added item to the list, id: %s, name: %s' % (new_index, name)}

class TodoResource(Resource):
    
    def get(self, todo_id):
        if int(todo_id) in todos:
            return todos[int(todo_id)]
        else:
            return "Item not in list"

    def put(self, todo_id):
        if int(todo_id) in todos:
            data = request.get_json()
            timestamp = datetime.now()
            todo = todos[int(todo_id)]
            todo["title"] = data["title"]
            todo["due_date"] = data["due_date"]
            todo["completed"] = data["completed"]
            todo["last_updated_date"] = str(timestamp)
            if todo["completed"] == True:
                todo["completion_date"] = str(timestamp)
            else:
                todo["completion_date"] = "incomplete"
            return todo
        else:
            return "Nothing to update"

    def delete(self, todo_id):
        if int(todo_id) in todos:
            del todos[int(todo_id)]
            return {'message': 'Delete an item id: %s' % (todo_id)}
        else:
            return "Nothing to delete"

api.add_resource(TodoResource, '/todo/<todo_id>')
api.add_resource(TodoListResource, '/todos')

if __name__ == '__main__':
     app.run(debug=True)


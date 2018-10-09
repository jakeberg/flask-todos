from flask import Flask, request
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)

from datetime import datetime, date
import json
import logging
from logging.handlers import RotatingFileHandler

from todos import todos

# Builds custom logger
LOGFILE = "./todos.log"
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(filename)s : %(message)s')
r_logger = RotatingFileHandler(LOGFILE, mode='a', maxBytes=5*1024*1024, 
                                 backupCount=2, encoding=None, delay=0)
r_logger.setFormatter(formatter)
logger.addHandler(r_logger)
logger.setLevel(logging.INFO)

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('due_date')
parser.add_argument('completed')

class TodoListResource(Resource):

    def get(self):
        return todos_list_get()


    def post(self):
        return todos_list_post()


def todo_list_get():
    logger.info("User ")
    try:
        logger.info("User accessed all todos")
        return todos
    except:
        logger.error("User accessed all todos")
        return "Something happened and request was not made..."


def todo_list_post():
    timestamp = datetime.now()
    args = parser.parse_args()
    new_todo = {
        "title": args["title"],
        "creation_date": str(timestamp),
        "last_updated_date": str(timestamp),
        "due_date": args["due_date"],
        "completed": args["completed"],
        "completion_date": "incomplete"
        }
    new_index = len(todos) + 1
    todos[new_index] = new_todo
    name = todos.get("title", args["title"])
    if name:
        return {
            'message': 'Added item to the list, id: %s, name: %s' % (new_index, name)
            }

#------------------------------------------------------------------------------------


class TodoResource(Resource):
    
    def get(self, todo_id):
        return todo_get(todo_id)

    def put(self, todo_id):
        args = parser.parse_args()
        return todo_put(todo_id, args)

    def delete(self, todo_id):
        return todo_delete(todo_id)


# The functionality of these have been broken out for testing 
def todo_get(todo_id):
    if int(todo_id) in todos:
        return todos[int(todo_id)]
    else:
        return "Item not in list"


def todo_put(todo_id, args):
    if int(todo_id) in todos:
        timestamp = datetime.now()
        todo = todos[int(todo_id)]
        todo["title"] = args["title"]
        todo["due_date"] = args["due_date"]
        todo["completed"] = args["completed"]
        todo["last_updated_date"] = str(timestamp)
        if todo["completed"] == True:
            todo["completion_date"] = str(timestamp)
        else:
            todo["completion_date"] = "incomplete"
        return todo
    else:
        return "Nothing to update"


def todo_delete(todo_id):
    if int(todo_id) in todos:
        del todos[int(todo_id)]
        return {'message': 'Delete an item id: %s' % (todo_id)}
    else:
        return "Nothing to delete"


api.add_resource(TodoResource, '/todo/<todo_id>')
api.add_resource(TodoListResource, '/todos')

if __name__ == '__main__':
     app.run(debug=True)


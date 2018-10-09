from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from create_app import app, api
from datetime import datetime, date
import json
import logging
from logging.handlers import RotatingFileHandler
from unittest.mock import MagicMock

from todos import todos

# Builds custom logger
LOGFILE = "./todos.log"
logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '%(asctime)s : %(levelname)s : %(filename)s : %(message)s'
    )
r_logger = RotatingFileHandler(
    LOGFILE, mode='a',
    maxBytes=5*1024*1024,
    backupCount=2,
    encoding=None,
    delay=0
    )
r_logger.setFormatter(formatter)
logger.addHandler(r_logger)
logger.setLevel(logging.INFO)

# Parser
parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('due_date')
parser.add_argument('completed')


class TodoListResource(Resource):

    def get(self):
        """
        Abstracted logic for testing purposes
        """
        return todos_list_get()

    def post(self):
        """
        Abstracted logic for testing purposes
        """
        args = parser.parse_args()
        return todos_list_post(args)


def todo_list_get():
    logger.info("User ")
    try:
        logger.info("User accessed all todos")
        return todos
    except:
        logger.error("User accessed all todos")
        return "Something happened and request was not made..." \
            "-- todo_list_get()"


def todo_list_post(args):
    timestamp = datetime.now()
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
            "message":
            "Added item to the list, id: %s, name: %s" % (new_index, name),
            "name": name
            }
    else:
        return "Something went wrong. -- todo_list_parse()"


class TodoResource(Resource):

    def get(self, todo_id):
        """
        Abstracted logic for testing purposes
        """
        return todo_get(todo_id)

    def put(self, todo_id):
        """
        Abstracted logic for testing purposes
        """
        args = parser.parse_args()
        return todo_put(todo_id, args)

    def delete(self, todo_id):
        """
        Abstracted logic for testing purposes
        """
        return todo_delete(todo_id)


def todo_get(todo_id):
    if int(todo_id) in todos:
        return todos[int(todo_id)]
    else:
        return "Item not in list. -- todo_get()"


def todo_put(todo_id, args):
    if int(todo_id) in todos:
        timestamp = datetime.now()
        todo = todos[int(todo_id)]
        todo["title"] = args["title"]
        todo["due_date"] = args["due_date"]
        todo["completed"] = args["completed"]
        todo["last_updated_date"] = str(timestamp)
        if todo["completed"] is True:
            todo["completion_date"] = str(timestamp)
        else:
            todo["completion_date"] = "incomplete"
        return todo
    else:
        return "Nothing to update. -- todo_put()"


def todo_delete(todo_id):
    if int(todo_id) in todos:
        del todos[int(todo_id)]
        return {'message': 'Delete an item id: %s' % (todo_id)}
    else:
        return "Nothing to delete. -- todo_delete()"


api.add_resource(TodoResource, '/todo/<todo_id>')
api.add_resource(TodoListResource, '/todos')


if __name__ == '__main__':
    app.run(debug=True)

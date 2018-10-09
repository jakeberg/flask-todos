from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__)
    api = Api(app)
    return app, api

app, api = create_app()

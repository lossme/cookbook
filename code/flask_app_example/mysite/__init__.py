from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


api = Api(prefix='/api')
db = SQLAlchemy()


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)

    from .resources.todo import TodoApi
    api.add_resource(TodoApi, '/todo/')
    api.init_app(app)

    return app

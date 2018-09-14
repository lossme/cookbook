from flask import Flask
from flask_restful import Api
from flask_celery import Celery


api = Api()
celery = Celery()


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    api.init_app(app)
    celery.init_app(app)
    init_route(app, api)

    return app


def init_route(app, api):
    from .index import Hello, HelloTaskStatus
    api.add_resource(Hello, '/hello/<string:name>', endpoint='hello')
    api.add_resource(HelloTaskStatus, '/hello/status/<string:task_id>', endpoint='hello_status')
    api.init_app(app)

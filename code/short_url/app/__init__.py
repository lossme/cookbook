from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


api = Api()
db = SQLAlchemy()


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)

    from .resources.short_url import Encode, Decode
    api.add_resource(Encode, '/encode/', strict_slashes=False)
    api.add_resource(Decode, '/<string:short_url>', strict_slashes=False)
    api.init_app(app)

    return app

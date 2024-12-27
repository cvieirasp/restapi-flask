from flask import Flask
from flask_restful import Api
from application.data.db import db
from application.resources.user_resource import UserList, User

api = Api()


def create_app():
    app = Flask(__name__)
    app.config.from_object('application.config.Config')

    db.init_app(app)

    api.add_resource(UserList, '/users')
    api.add_resource(User, '/users/<string:cpf>')

    api.init_app(app)

    return app

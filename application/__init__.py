from flask import Flask
from flask_restful import Api
from application.data.db import db
from application.resources.user_resource import UserList, User


def create_app(dbconfig):
    app = Flask(__name__)
    app.config.from_object(dbconfig)
    api = Api()

    db.init_app(app)

    api.add_resource(UserList, '/users')
    api.add_resource(User, '/users/<string:cpf>')

    api.init_app(app)

    return app

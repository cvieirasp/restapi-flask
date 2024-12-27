from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'usersdb',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'
}

api = Api(app)
db = MongoEngine(app)


# Configuração do banco de dados
class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)


# Recurso para /users
class UserList(Resource):
    def get(self):
        return {
            'users': ['user1', 'user2', 'user3']
        }

    def post(self):
        return {
            'message': 'User created'
        }


# Recurso para /users/{cpf}
class User(Resource):
    def get(self, cpf):
        return {
            'user': cpf
        }


api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

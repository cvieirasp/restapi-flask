from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


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

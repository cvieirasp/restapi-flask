from flask import Flask, jsonify
from flask_restful import Api, reqparse, Resource
from flask_mongoengine import MongoEngine
from mongoengine import NotUniqueError

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


_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    'first_name', type=str, required=True, help='This field cannot be blank'
)
_user_parser.add_argument(
    'last_name', type=str, required=True, help='This field cannot be blank'
)
_user_parser.add_argument(
    'email', type=str, required=True, help='This field cannot be blank'
)
_user_parser.add_argument(
    'birth_date', type=str, required=True, help='This field cannot be blank'
)
_user_parser.add_argument(
    'cpf', type=str, required=True, help='This field cannot be blank'
)


# Configuração do banco de dados
class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)

    def to_json_obj(self):
        return {
            'id': str(self.id),
            'cpf': self.cpf,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'birth_date': self.birth_date
        }


# Recurso para /users
class UserList(Resource):
    def validate_cpf(self, cpf):
        if cpf.isdigit() and len(cpf) == 11:
            return True
        return False

    def get(self):
        return jsonify(UserModel.objects())

    def post(self):
        data = _user_parser.parse_args()

        if not self.validate_cpf(data['cpf']):
            return {
                'message': 'CPF is Invalid!'
            }, 400

        user = UserModel(**data)
        try:
            user.save()
            return user.to_json_obj(), 201
        except NotUniqueError:
            return {
                'message': 'A user with CPF %s already exists!' % user.cpf
            }, 400


# Recurso para /users/{cpf}
class User(Resource):
    def get(self, cpf):
        user = UserModel.objects(cpf=cpf).first()
        if user:
            return jsonify(user)
        return {'message': 'User not found!'}, 404


api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

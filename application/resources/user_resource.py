from flask import jsonify
from flask_restful import reqparse, Resource
from application.services.user_service import UserService
from application.validators.cpf_validator import validate_cpf

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


class UserList(Resource):
    def get(self):
        users = UserService.get_all_users()
        return jsonify(users)

    def post(self):
        data = _user_parser.parse_args()
        if not validate_cpf(data['cpf']):
            return {'message': 'CPF is Invalid!'}, 400

        try:
            user = UserService.create_user(data)
            return user.to_json_obj(), 201
        except ValueError as e:
            return {'message': str(e)}, 400


class User(Resource):
    def get(self, cpf):
        user = UserService.get_user_by_cpf(cpf)
        if user:
            return jsonify(user)
        return {'message': 'User not found!'}, 404

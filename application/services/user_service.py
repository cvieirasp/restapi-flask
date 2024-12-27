from application.models.user import UserModel
from mongoengine import NotUniqueError


class UserService:
    @staticmethod
    def get_all_users():
        return UserModel.objects()

    @staticmethod
    def get_user_by_cpf(cpf):
        return UserModel.objects(cpf=cpf).first()

    @staticmethod
    def create_user(data):
        user = UserModel(**data)
        try:
            user.save()
            return user
        except NotUniqueError:
            raise ValueError(f"A user with CPF {data['cpf']} already exists!")

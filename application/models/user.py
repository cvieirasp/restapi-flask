from application.data.db import db


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

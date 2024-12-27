import pytest
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('tests.Config')
        with app.test_client() as client:
            yield client

    @pytest.fixture
    def valid_user(self):
        return {
            "cpf": "12345678901",
            "first_name": "User",
            "last_name": "Test",
            "email": "user@mail.com",
            "birth_date": "1990-05-30"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "cpf": "invalid_cpf",
            "first_name": "User",
            "last_name": "Test",
            "email": "user@mail.com",
            "birth_date": "1990-05-30"
        }

    def test_get_users_success(self, client):
        response = client.get('/users')
        assert response.status_code == 200
        assert response.json == []

    def test_post_user_success(self, client, valid_user):
        response = client.post('/users', json=valid_user)
        assert response.status_code == 201
        assert response.json['cpf'] == valid_user.get('cpf')
        assert response.json['email'] == valid_user.get('email')
        assert response.json['first_name'] == valid_user.get('first_name')
        assert response.json['last_name'] == valid_user.get('last_name')

    def test_post_invalid_user_cpf(self, client, invalid_user):
        response = client.post('/users', json=invalid_user)
        assert response.status_code == 400
        assert response.json['message'] == 'CPF is Invalid!'

    def test_post_user_cpf_exists(self, client, valid_user):
        client.post('/users', json=valid_user)

        response = client.post('/users', json=valid_user)
        assert response.status_code == 400
        assert response.json['message'] == 'A user with CPF %s already exists!' % valid_user.get('cpf')

    def test_get_user_by_cpf_success(self, client, valid_user):
        client.post('/users', json=valid_user)

        response = client.get('/users/%s' % valid_user.get('cpf'))
        assert response.status_code == 200
        assert response.json['cpf'] == valid_user.get('cpf')
        assert response.json['email'] == valid_user.get('email')
        assert response.json['first_name'] == valid_user.get('first_name')
        assert response.json['last_name'] == valid_user.get('last_name')

    def test_get_user_by_cpf_not_found(self, client):
        response = client.get('/users/98765432101')
        assert response.status_code == 404
        assert response.json['message'] == 'User not found!'
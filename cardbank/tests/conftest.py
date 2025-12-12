import pytest
import json
from faker import Faker

from gasto.models import Cardbank

def _get_token(client, user):
    data = {
        "username": user.username,
        "password": "strong-test-pass",
    }
    response = client.post("/api/v1/auth/token", data, content_type='application/json')
    result = json.loads(response.content)
    return result["access"]


@pytest.fixture
def create_user(django_user_model):
    user_data = {
        'username': 'Lorem',
        'password': 'strong-test-pass',
    }
    user = django_user_model.objects.create_user(**user_data)
    return user


@pytest.fixture
def auth_headers(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="teste-user",
        password="strong-test-pass"
    )
    token = _get_token(client, user)
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def new_data():
    return {'name': 'BB-cartões'}

@pytest.fixture
def new_update_data():
    return {
        'id': 1,
        'name': 'Citibank'
    }

@pytest.fixture
def create_datas(new_data):
    faker = Faker()
    faker.name()
    for _ in range(5):
        Cardbank.objects.create(name=faker.name())
    cardbanks = Cardbank.objects.all()
    return cardbanks

@pytest.fixture
def create_data(new_data):
    cardbank = Cardbank.objects.create(**new_data)
    return cardbank


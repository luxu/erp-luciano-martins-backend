import pytest
from faker import Faker

from gasto.models import Segmento


@pytest.fixture
def new_update_data():
    return {
        'id': 1,
        'name': 'Padarias'
    }


@pytest.fixture
def new_data():
    return {'name': 'Supermercados'}


@pytest.fixture
def create_datas():
    faker = Faker()
    faker.name()
    for _ in range(5):
        Segmento.objects.create(name=faker.name())
    cardbanks = Segmento.objects.all()
    return cardbanks


@pytest.fixture
def create_user(django_user_model, user_data):
    user = django_user_model.objects.create_user(**user_data)
    return user


@pytest.fixture
def create_data(new_data):
    segmento = Segmento.objects.create(**new_data)
    return segmento

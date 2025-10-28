import pytest
from faker import Faker

from gasto.models import Cardbank


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


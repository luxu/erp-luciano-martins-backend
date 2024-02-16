import pytest

from gasto.models import Segmento


@pytest.fixture
def user_data():
    return {
        'username': 'Lorem',
        'password': 'strong-test-pass',
    }

@pytest.fixture
def segmento_data():
    return {
        'name': 'Supermercados',
    }

@pytest.fixture
def user(django_user_model, user_data):
    return django_user_model.objects.create_user(**user_data)

@pytest.fixture
def segmento(segmento_data):
    return Segmento.objects.create(**segmento_data)

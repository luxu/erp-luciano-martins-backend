import pytest

from gasto.models import Cardbank


@pytest.fixture
def user_data():
    return {
        'username': 'Lorem',
        'password': 'strong-test-pass',
    }

@pytest.fixture
def cardbank_data():
    return {
        'name': 'BB-cartões',
    }

@pytest.fixture
def user(django_user_model, user_data):
    return django_user_model.objects.create_user(**user_data)

@pytest.fixture
def cardbank(cardbank_data):
    return Cardbank.objects.create(**cardbank_data)

from datetime import datetime

import pytest

from gasto.models import Gasto, Segmento, Cardbank


@pytest.fixture
def user_data():
    return {
        'username': 'Lorem',
        'password': 'strong-test-pass',
    }

@pytest.fixture
def gasto_data():
    Segmento.objects.create(name="Supermercados")
    Cardbank.objects.create(name="BB")
    return {
        'name': 'Nagai',
        'datagasto': datetime.now().date(),
        'total': "10.00",
        'segmento_id': 1,
        'card_bank_id': 1,
        'opcoes_cartao': "C",
    }
@pytest.fixture
def gasto_data_update():
    Segmento.objects.create(name="Supermercados")
    Cardbank.objects.create(name="BB")
    return {
        'name': 'Estrela',
        'datagasto': datetime.now().date(),
        'total': "10.00",
        'segmento_id': 1,
        'card_bank_id': 1,
        'opcoes_cartao': "C",
    }

@pytest.fixture
def user(django_user_model, user_data):
    return django_user_model.objects.create_user(**user_data)

@pytest.fixture
def gasto():
    dados = gasto_data()
    return Gasto.objects.create(**dados)

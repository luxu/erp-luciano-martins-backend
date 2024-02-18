from datetime import datetime, timedelta

import pytest

from gasto.models import Segmento, Cardbank, Parcelas

from gasto.tests.conftest import gasto

@pytest.fixture
def user_data():
    return {
        'username': 'Lorem',
        'password': 'strong-test-pass',
    }

@pytest.fixture
def parcela_data(gasto):
    return {
        'gasto_id': 1,
        'parcelas': 5,
        'numero_parcela': 1,
        'valor_parcela': "10.00",
        'data_parcela': datetime.now().date(),
    }

@pytest.fixture
def parcelas_data(gasto):
    data = datetime.now().date()
    quantidade_parcelas = 5
    for nro_parcela in range(quantidade_parcelas):
        Parcelas.objects.create(
            gasto_id=1,
            parcelas=quantidade_parcelas,
            numero_parcela=nro_parcela,
            valor_parcela="10.00",
            data_parcela=data,
        )
        data = data + timedelta(days=30)


@pytest.fixture
def parcela_data_update():
    Segmento.objects.create(name="Supermercados")
    Cardbank.objects.create(name="BB")
    return {
        'gasto': 'Nagai',
        'parcelas': datetime.now().date(),
        'numero_parcela': "10.00",
        'valor_parcela': 1,
        'data_parcela': 1,
    }

@pytest.fixture
def user(django_user_model, user_data):
    return django_user_model.objects.create_user(**user_data)

@pytest.fixture
def parcela(parcela_data):
    return Parcelas.objects.create(**parcela_data)

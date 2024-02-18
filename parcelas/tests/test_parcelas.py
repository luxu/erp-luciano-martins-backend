import json
from http import HTTPStatus

import pytest

URL = '/api/v1/parcelas'

def authorization(client, user):
    client.force_login(user)
    token = get_token(client, user)
    headers = {'Authorization': f'Bearer {token["access"]}'}
    return headers


def get_token(client, user):
    data = {
        'username': user.username,
        'password': 'strong-test-pass',
    }
    response = client.post(
        '/api/v1/token/pair',
        data,
        content_type='application/json'
    )
    return json.loads(response.content)

@pytest.mark.django_db
def test_list_parcelas(client, user, parcela):
    response = client.get(
        URL,
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 0

@pytest.mark.django_db
def test_list_parcelas(client, user, parcelas_data):
    response = client.get(
        URL,
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 5
    total = 0
    for parcela in response.json():
        total += float(parcela['valor_parcela'])
    assert total == 50.00
@pytest.mark.django_db
def test_create_parcela(client, user, parcela_data):
    # headers = authorization(client, user)
    response = client.post(
        URL,
        parcela_data,
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.OK

@pytest.mark.django_db
def test_update_parcela(client, user, parcela, parcela_data_update):
    headers = authorization(client, user)
    response = client.patch(
        f'{URL}/{parcela.id}',
        data=parcela_data_update,
        content_type='application/json',
        headers=headers
    )
    expected = {'name': 'Estrela'}
    assert response.status_code == HTTPStatus.OK
    assert response.json()['name'] == expected['name']




@pytest.mark.django_db
def test_delete_parcela(client, user, parcela):
    headers = authorization(client, user)
    response = client.delete(
        f'{URL}/{parcela.id}',
        content_type='application/json',
        headers=headers
    )
    assert response.status_code == HTTPStatus.NO_CONTENT

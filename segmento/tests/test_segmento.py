import json
from http import HTTPStatus
import pytest

def get_token(client, user):
    data = {
        'username': user.username,
        'password': 'strong-test-pass',
    }
    response = client.post('/api/v1/token/pair', data, content_type='application/json')
    return json.loads(response.content)
@pytest.mark.django_db
def test_list_segmento(client, segmento):
    response = client.get('/api/v1/segmentos', content_type='application/json')
    expected = {'id': 1, 'name': 'Supermercados',}
    assert response.status_code == HTTPStatus.OK
    assert expected == response.json()[0]

@pytest.mark.django_db
def test_create_segmento(client, user, segmento_data):
    client.force_login(user)
    token = get_token(client, user)
    headers = {'Authorization': f'Bearer {token["access"]}'}
    response = client.post('/api/v1/cardbanks', segmento_data, content_type='application/json', headers=headers)
    expected = {'id': 1, 'name': 'Supermercados',}
    assert response.status_code == HTTPStatus.CREATED
    assert expected == response.json()

@pytest.mark.django_db
def test_update_segmento(client, user, segmento):
    client.force_login(user)
    token = get_token(client, user)
    headers = {'Authorization': f'Bearer {token["access"]}'}
    data = {'name': 'Farmácias'}
    response = client.patch(
        f'/api/v1/segmentos/{segmento.id}', data=data, content_type='application/json', headers=headers
    )
    expected = {'id': 1, 'name': 'Farmácias',}
    assert response.status_code == HTTPStatus.OK
    assert expected == json.loads(response.content)

@pytest.mark.django_db
def test_delete_segmento(client, user, segmento):
    client.force_login(user)
    token = get_token(client, user)
    headers = {'Authorization': f'Bearer {token["access"]}'}
    response = client.delete(
        f'/api/v1/segmentos/{segmento.id}', content_type='application/json', headers=headers
    )
    assert response.status_code == HTTPStatus.NO_CONTENT

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
def test_list_cardbank(client, cardbank):
    response = client.get('/api/v1/cardbanks', content_type='application/json')
    expected = {'id': 1, 'name': 'BB-cartões',}
    assert response.status_code == HTTPStatus.OK
    assert expected == response.json()[0]

@pytest.mark.django_db
def test_create_cardbank(client, user, cardbank_data):
    client.force_login(user)
    token = get_token(client, user)
    headers = {'Authorization': f'Bearer {token["access"]}'}
    response = client.post('/api/v1/cardbanks', cardbank_data, content_type='application/json', headers=headers)
    expected = {'id': 1, 'name': 'BB-cartões',}
    assert response.status_code == HTTPStatus.CREATED
    assert expected == response.json()

@pytest.mark.django_db
def test_update_cardbank(client, user, cardbank):
    client.force_login(user)
    token = get_token(client, user)
    headers = {'Authorization': f'Bearer {token["access"]}'}
    data = {'name': 'BB'}
    response = client.patch(
        f'/api/v1/cardbanks/{cardbank.id}', data=data, content_type='application/json', headers=headers
    )
    expected = {'id': 1, 'name': 'BB'}
    assert response.status_code == HTTPStatus.OK
    assert expected == json.loads(response.content)

@pytest.mark.django_db
def test_delete_cardbank(client, user, cardbank):
    client.force_login(user)
    token = get_token(client, user)
    headers = {'Authorization': f'Bearer {token["access"]}'}
    response = client.delete(
        f'/api/v1/cardbanks/{cardbank.id}', content_type='application/json', headers=headers
    )
    assert response.status_code == HTTPStatus.NO_CONTENT

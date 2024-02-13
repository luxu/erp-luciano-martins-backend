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
def test_list_users_with_token(client, user):
    client.force_login(user)
    token = get_token(client, user)
    headers = {'Authorization': f'Bearer {token["access"]}'}
    response = client.get('/api/v1/users', headers=headers)
    assert response.status_code == HTTPStatus.OK

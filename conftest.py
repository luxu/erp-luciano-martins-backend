import json
import pytest

@pytest.fixture
def create_user(django_user_model):
    user_data = {
        'username': 'Lorem',
        'password': 'strong-test-pass',
    }
    user = django_user_model.objects.create_user(**user_data)
    return user

@pytest.fixture
def auth_headers(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="teste-user",
        password="strong-test-pass"
    )
    token = _get_token(client, user)
    return {"Authorization": f"Bearer {token}"}


def _get_token(client, user):
    data = {
        "username": user.username,
        "password": "strong-test-pass",
    }
    response = client.post("/api/v1/auth/token", data, content_type='application/json')
    result = json.loads(response.content)
    return result["access"]

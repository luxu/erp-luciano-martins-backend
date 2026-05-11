import json
from http import HTTPStatus
import pytest
from django.urls import reverse_lazy

app_name = 'cardbank'
URL_LIST = reverse_lazy(f'api-1.0.0:list_{app_name}')
URL_CREATE = reverse_lazy(f'api-1.0.0:create_{app_name}')

URL_UPDATE = reverse_lazy(f'api-1.0.0:update_{app_name}', kwargs={f"{app_name}_id": 1})
URL_DELETE = reverse_lazy(f'api-1.0.0:delete_{app_name}', kwargs={f"{app_name}_id": 1})


@pytest.mark.django_db
def test_list(client, auth_headers):
    response = client.get(URL_LIST, headers=auth_headers)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_list_by_id(client, create_datas, auth_headers):
    list_ids = [data.id for data in create_datas]
    choice_id = list_ids[2]
    URL_LIST_BY_ID = reverse_lazy(f'api-1.0.0:get_{app_name}', kwargs={f"{app_name}_id": choice_id})
    response = client.get(URL_LIST_BY_ID, headers=auth_headers)
    assert response.status_code == HTTPStatus.OK
    assert response.json()['id'] == choice_id


@pytest.mark.django_db
def test_create(client, new_data, auth_headers):
    response = client.post(URL_CREATE, new_data, content_type='application/json', headers=auth_headers)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['id'] == 1


@pytest.mark.django_db
def test_update(client, auth_headers, create_data, new_update_data):
    response = client.patch(URL_UPDATE, data=new_update_data, content_type='application/json', headers=auth_headers)
    assert response.status_code == HTTPStatus.OK
    assert json.loads(response.content)['id'] == new_update_data['id']


@pytest.mark.django_db
def test_delete(client, auth_headers, create_data):
    response = client.delete(URL_DELETE, content_type='application/json', headers=auth_headers)
    assert response.status_code == HTTPStatus.NO_CONTENT

from http import HTTPStatus
from typing import List

from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.tokens import default_token_generator
from ninja import Router
from ninja.security import django_auth

from .models import User

from .schemas import LoginSchema, UserOutSchema

router = Router(tags=['Accounts'])

# TODO
_LOGIN_BACKEND = 'django.contrib.auth.backends.ModelBackend'


@router.post(
    'auth/login', response={HTTPStatus.OK: UserOutSchema, HTTPStatus.FORBIDDEN: None}, auth=None, tags=['Auth']
)  # noqa E501
def login(request, data: LoginSchema):
    user = authenticate(backend=_LOGIN_BACKEND, **data.dict())

    if user is not None and user.is_active:
        django_login(request, user, backend=_LOGIN_BACKEND)
        return user

    return HTTPStatus.FORBIDDEN, None


@router.get('auth/logout', response={HTTPStatus.NO_CONTENT: None}, auth=django_auth, tags=['Auth'])
def logout(request):
    django_logout(request)
    return HTTPStatus.NO_CONTENT, None


@router.get('users', tags=['Users'], response=List[UserOutSchema])
def list_users(request):
    qs = User.objects.all()
    return qs

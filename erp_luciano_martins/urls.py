from typing import List

from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.urls import path
from ninja import NinjaAPI, Schema
from ninja.security import HttpBearer

from gasto.models import Cardbank

api = NinjaAPI()


class HelloSchema(Schema):
    name: str = "world"


class UserSchema(Schema):
    username: str
    email: str
    first_name: str
    last_name: str


class CardbankIn(Schema):
    name: str


class CardbankOut(Schema):
    id: int
    name: str


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


@api.get("/cardbanks", response=List[CardbankOut])
def list_cardbank(request):
    qs = Cardbank.objects.all()
    return qs


@api.get("/cardbanks/{cardbank_id}", response=CardbankOut)
def get_cardbank(request, cardbank_id: int):
    cardbank = get_object_or_404(Cardbank, id=cardbank_id)
    return cardbank


@api.post("/cardbanks", auth=AuthBearer())
def create_cardbank(request, payload: CardbankIn):
    cardbank = Cardbank.objects.create(**payload.dict())
    return {"id": cardbank.id}


@api.put("/cardbanks/{cardbank_id}", auth=AuthBearer())
def update_cardbank(request, cardbank_id: int, payload: CardbankIn):
    cardbank = get_object_or_404(Cardbank, id=cardbank_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(cardbank, attr, value)
    cardbank.save()
    return {"success": True}


@api.delete("/cardbanks/{cardbank_id}", auth=AuthBearer())
def delete_cardbank(request, cardbank_id: int):
    cardbank = get_object_or_404(Cardbank, id=cardbank_id)
    cardbank.delete()
    return {"success": True}


@api.get("/me", response=UserSchema)
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

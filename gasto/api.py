from typing import List
from http import HTTPStatus

from ninja import Router
from ninja_jwt.authentication import JWTAuth

from django.shortcuts import get_object_or_404

from .schemas import CardbankSchema, CardbankCreateSchema

router = Router(tags=['Gasto'])


from gasto.models import Cardbank


@router.get("cardbanks", response=list[CardbankSchema], by_alias=True)
def list_cardbank(request):
    return Cardbank.objects.all()

@router.get("cardbanks/{cardbank_id}", response=CardbankSchema, auth=JWTAuth())
def get_cardbank(request, cardbank_id: int):
    return get_object_or_404(Cardbank, id=cardbank_id)


@router.post('cardbanks', response={HTTPStatus.CREATED: CardbankSchema}, auth=JWTAuth())
def create_cardbank(request, payload: CardbankCreateSchema):
    return Cardbank.objects.create(**payload.dict())

@router.patch("cardbanks/{cardbank_id}", response=CardbankSchema)
def update_cardbank(request, cardbank_id: int, payload: CardbankCreateSchema):
    instance = get_object_or_404(Cardbank, id=cardbank_id)
    data = payload.dict()

    for attr, value in data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance

@router.delete("cardbanks/{cardbank_id}", response={HTTPStatus.NO_CONTENT: None})
def delete_cardbank(request, cardbank_id: int):
    cardbank = get_object_or_404(Cardbank, id=cardbank_id)
    cardbank.delete()
    return HTTPStatus.NO_CONTENT, None

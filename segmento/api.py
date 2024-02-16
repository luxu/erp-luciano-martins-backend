from http import HTTPStatus

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja_jwt.authentication import JWTAuth

from .schemas import SegmentoSchema, SegmentoCreateSchema

router = Router(tags=['Segmento'])

from gasto.models import Segmento


@router.get("segmentos", response=list[SegmentoSchema], by_alias=True)
def list_segmento(request):
    return Segmento.objects.all()


@router.get("segmentos/{segmento_id}", response=SegmentoSchema, auth=JWTAuth())
def get_segmento(request, segmento_id: int):
    return get_object_or_404(Segmento, id=segmento_id)


@router.post('segmentos', response={HTTPStatus.CREATED: SegmentoSchema})
def create_segmento(request, payload: SegmentoCreateSchema):
    return Segmento.objects.create(**payload.dict())


@router.patch("segmentos/{segmento_id}", response=SegmentoSchema, auth=JWTAuth())
def update_segmento(request, segmento_id: int, payload: SegmentoCreateSchema):
    instance = get_object_or_404(Segmento, id=segmento_id)
    data = payload.dict()

    for attr, value in data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance


@router.delete("segmentos/{segmento_id}", response={HTTPStatus.NO_CONTENT: None}, auth=JWTAuth())
def delete_segmento(request, segmento_id: int):
    segmento = get_object_or_404(Segmento, id=segmento_id)
    segmento.delete()
    return HTTPStatus.NO_CONTENT, None

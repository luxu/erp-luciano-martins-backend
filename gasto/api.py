from http import HTTPStatus

from django.shortcuts import get_object_or_404

from ninja import Router

from ninja_jwt.authentication import JWTAuth

from gasto.models import Gasto

from .schemas import GastoCreateSchema, GastoSchema

router = Router(tags=['Gasto'])



@router.get("gastos", response=list[GastoSchema])
def list_gasto(request):
    return Gasto.objects.all()


@router.get("gastos/{gasto_id}", response=GastoCreateSchema, auth=JWTAuth())
def get_gasto(request, gasto_id: int):
    return get_object_or_404(Gasto, id=gasto_id)


@router.post('gastos', response={HTTPStatus.CREATED: GastoSchema}, auth=JWTAuth())
def create_gasto(request, gasto: GastoCreateSchema):
    gasto_data = gasto.model_dump()
    gasto_model = Gasto.objects.create(**gasto_data)
    return gasto_model


@router.patch("gastos/{gasto_id}", response={HTTPStatus.OK: GastoSchema}, auth=JWTAuth())
def update_gasto(request, gasto_id: int, payload: GastoCreateSchema):
    instance = get_object_or_404(Gasto, id=gasto_id)
    data = payload.dict()

    for attr, value in data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance


@router.delete("gastos/{gasto_id}", response={HTTPStatus.NO_CONTENT: None}, auth=JWTAuth())
def delete_cardbank(request, gasto_id: int):
    instance = get_object_or_404(Gasto, id=gasto_id)
    instance.delete()
    return HTTPStatus.NO_CONTENT, None

from http import HTTPStatus

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja_jwt.authentication import JWTAuth
from ninja.pagination import paginate, PageNumberPagination

from gasto.models import Parcelas

router = Router(tags=['Parcelas'])

from .schemas import ParcelasSchema, ParcelaSchema, ParcelasLoteCreateSchema


@router.get("parcelas", response=list[ParcelasSchema], auth=JWTAuth())
@paginate(PageNumberPagination, page_size=10)
def list_parcelas(request):
    return Parcelas.objects.all()


@router.get("parcelas/{parcela_id}", response=ParcelaSchema, auth=JWTAuth())
def get_parcelas(request, parcela_id: int):
    return get_object_or_404(Parcelas, id=parcela_id)

@router.post('parcelas/lote', auth=JWTAuth())
def create_parcelas_lote(request, payload: ParcelasLoteCreateSchema):
    itens = []

    for item in payload.parcelas:
        itens.append(
            Parcelas(
                gasto_id=item.gasto_id,
                parcelas=item.parcelas,
                numero_parcela=item.numero_parcela,
                valor_parcela=item.valor_parcela,
                data_parcela=item.data_parcela,
            )
        )

    Parcelas.objects.bulk_create(itens)
    return {'message': 'Parcelas criadas com sucesso'}


# @router.patch("cardbanks/{cardbank_id}", response=SegmentoSchema, auth=JWTAuth())
# def update_cardbank(request, cardbank_id: int, payload: CardbankCreateSchema):
#     instance = get_object_or_404(Cardbank, id=cardbank_id)
#     data = payload.dict()
#
#     for attr, value in data.items():
#         setattr(instance, attr, value)
#     instance.save()
#     return instance
#
#
# @router.delete("cardbanks/{cardbank_id}", response={HTTPStatus.NO_CONTENT: None}, auth=JWTAuth())
# def delete_cardbank(request, cardbank_id: int):
#     cardbank = get_object_or_404(Cardbank, id=cardbank_id)
#     cardbank.delete()
#     return HTTPStatus.NO_CONTENT, None

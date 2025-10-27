from http import HTTPStatus

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja_jwt.authentication import JWTAuth
from ninja.pagination import paginate, PageNumberPagination


from gasto.models import Parcelas

router = Router(tags=['Parcelas'])

from .schemas import ParcelasSchema




@router.get("parcelas", response=list[ParcelasSchema])
@paginate(PageNumberPagination, page_size=10)
def list_parcelas(request):
    return Parcelas.objects.all()


# @router.get("cardbanks/{cardbank_id}", response=SegmentoSchema, auth=JWTAuth())
# def get_cardbank(request, cardbank_id: int):
#     return get_object_or_404(Cardbank, id=cardbank_id)


# @router.post('parcelas', response={HTTPStatus.CREATED: ParcelasSchema}) #, auth=JWTAuth())
# def create_parcela(request, payload: ParcelasCreateSchema):
#     return Parcelas.objects.create(**payload.dict())


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

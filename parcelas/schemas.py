import datetime

from ninja import ModelSchema, Schema

from gasto.models import Parcelas
from gasto.schemas import GastoSchema


class ParcelasSchema(ModelSchema):
    gasto: GastoSchema

    class Meta:
        model = Parcelas
        fields = [
            'id',
            'gasto',
            'parcelas',
            'numero_parcela',
            'valor_parcela',
            'data_parcela'
        ]

# class ParcelasCreateSchema(Schema):
#     gasto_id: int
#     parcelas: int
#     numero_parcela: int
#     valor_parcela: str
#     data_parcela: datetime

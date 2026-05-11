from datetime import date
from typing import List

from ninja import ModelSchema, Schema

from gasto.models import Parcelas, Gasto

class ParcelasSchema(ModelSchema):
    # gasto: Optional["GastoSchema"]

    class Meta:
        model = Parcelas
        fields = ['id', 'gasto', 'parcelas',
                  'numero_parcela', 'valor_parcela',
                  'data_parcela']

class ParcelaSchema(ModelSchema):

    class Meta:
        model = Parcelas
        fields = [
            'id',
            'gasto',
            'parcelas',
            'numero_parcela',
            'valor_parcela',
            'data_parcela',
        ]

class ParcelasCreateSchema(Schema):
    gasto_id: int
    parcelas: int
    numero_parcela: int
    valor_parcela: float
    data_parcela: date

class ParcelasLoteCreateSchema(Schema):
    parcelas: List[ParcelasCreateSchema]

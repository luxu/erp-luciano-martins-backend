from datetime import datetime

from ninja import ModelSchema, Schema

from gasto.models import Gasto, Segmento, Cardbank


class SegmentoSchema(ModelSchema):
    class Meta:
        model = Segmento
        fields = ['name']


class CardbankSchema(ModelSchema):
    class Meta:
        model = Cardbank
        fields = ['name']


class GastoSchema(ModelSchema):
    segmento: SegmentoSchema
    card_bank: CardbankSchema

    class Meta:
        model = Gasto
        fields = [
            'id',
            'name',
            'datagasto',
            'total',
            'description_on_invoice',
            'opcoes_cartao',
            'segmento',
            'card_bank'
        ]


class GastoCreateSchema(Schema):
    name: str
    datagasto: datetime
    total: str
    description_on_invoice: str = None
    opcoes_cartao: str
    segmento_id: int
    card_bank_id: int

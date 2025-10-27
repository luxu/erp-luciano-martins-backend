from typing import Optional

from ninja import ModelSchema

from cardbank.schemas import CardbankSchema
from gasto.models import Gasto, Parcelas
from segmento.schemas import SegmentoSchema


class GastoSchema(ModelSchema):
    segmento: SegmentoSchema
    card_bank: CardbankSchema
    description_on_invoice: Optional[str]

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

class ParcelaSchema(ModelSchema):
    gasto: GastoSchema

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

from datetime import date
from typing import Optional

from ninja import ModelSchema, Schema

from cardbank.schemas import CardbankSchema
from gasto.models import Gasto, Parcelas
from segmento.schemas import SegmentoSchema


class GastoIn(Schema):
    name: str
    datagasto: date  # Pydantic aceita o formato ISO 8601 (YYYY-MM-DD)
    # Recebe o ID do Segmento (int)
    segmento_id: int
    # Recebe o ID do CardBank (int)
    card_bank_id: int
    description_on_invoice: Optional[str] = None  # Se for opcional
    opcoes_cartao: Optional[str] = None  # Se for opcional
    more_infos: Optional[str] = None  # Se for opcional
    total: Optional[str] = None  # Se for opcional
    # Se você precisar de um 'id' para algum propósito, use Optional.
    # Se for um POST (criação), o ID será gerado pelo BD.
    # id: Optional[int] = None


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
            'more_infos',
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

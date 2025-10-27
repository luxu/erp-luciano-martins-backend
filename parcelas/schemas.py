import datetime
from typing import Optional

from ninja import ModelSchema, Schema

from gasto.models import Parcelas, Gasto
# from gasto.schemas import GastoSchema


class ParcelasSchema(ModelSchema):
    # gasto: Optional["GastoSchema"]

    class Meta:
        model = Parcelas
        fields = "__all__"

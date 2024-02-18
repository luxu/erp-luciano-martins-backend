from ninja import ModelSchema

from gasto.models import Segmento

class SegmentoSchema(ModelSchema):
    class Config:
        model = Segmento
        model_fields = ['id', 'name']
        populate_by_name = True

class SegmentoCreateSchema(ModelSchema):
    class Config:
        model = Segmento
        model_fields = ['name']

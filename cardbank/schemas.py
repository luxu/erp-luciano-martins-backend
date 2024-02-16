from ninja import ModelSchema

from gasto.models import Cardbank

class CardbankSchema(ModelSchema):
    class Config:
        model = Cardbank
        model_fields = ['id', 'name']
        populate_by_name = True

class CardbankCreateSchema(ModelSchema):
    class Config:
        model = Cardbank
        model_fields = ['name']

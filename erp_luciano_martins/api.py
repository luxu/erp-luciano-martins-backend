"""
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

api.add_router('', 'accounts.api.router')
api.add_router('', 'cardbank.api.router')
api.add_router('', 'gasto.api.router')
api.add_router('', 'segmento.api.router')
api.add_router('', 'parcelas.api.router')
"""

from ninja import NinjaAPI

from cardbank.api import router as cardbank_router
from segmento.api import router as segmento_router
from gasto.api import router as gasto_router
from parcelas.api import router as parcelas_router

api = NinjaAPI(csrf=True)

api.add_router("", cardbank_router, tags=["cardbank"])
api.add_router("", segmento_router, tags=["segmento"])
api.add_router("", gasto_router, tags=["gasto"])
api.add_router("", parcelas_router, tags=["parcelas"])

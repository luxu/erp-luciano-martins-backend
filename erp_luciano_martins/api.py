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
from ninja.security import django_auth

from ..cardbank.views import router as base_router
# from ..accounts.views import router as accounts_router
# from ..core.views import router as core_router

api = NinjaAPI(csrf=True)

api.add_router("/", base_router, tags=["base"])
# api.add_router("/accounts/", accounts_router, tags=["accounts"])
# api.add_router("/core/", core_router, auth=django_auth, tags=["core"])

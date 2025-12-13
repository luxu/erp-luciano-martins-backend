from ninja import NinjaAPI

from core.api import router as core_router
from cardbank.api import router as cardbank_router
from segmento.api import router as segmento_router
from gasto.api import router as gasto_router
from parcelas.api import router as parcelas_router

api = NinjaAPI(csrf=False)

api.add_router("", core_router, tags=["core"])
api.add_router("", gasto_router, tags=["gasto"])
api.add_router("", parcelas_router, tags=["parcelas"])
api.add_router("", segmento_router, tags=["segmento"])
api.add_router("", cardbank_router, tags=["cardbank"])

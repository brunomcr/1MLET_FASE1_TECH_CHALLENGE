from fastapi import FastAPI
from src.api.routes.root_router import root_router
from src.api.routes.production_router import production_router
from src.api.routes.processing_router import processing_router
from src.api.routes.trade_router import trade_router
from src.api.routes.import_router import import_router
from src.api.routes.export_router import export_router

app = FastAPI()

app.include_router(root_router)

app.include_router(production_router)

app.include_router(processing_router)

app.include_router(trade_router)

app.include_router(import_router)

app.include_router(export_router)

from fastapi import FastAPI
from src.api.routers import import_router, production_router, export_router, trading_router, processing_router
from src.dependencies import injector
from src.domain.interfaces import DBPopulatorService

print("Populating the database")
db_populator_service = injector.get(DBPopulatorService)
db_populator_service.populate()

print("Starting the application")
app = FastAPI()
app.include_router(export_router)
app.include_router(import_router)
app.include_router(processing_router)
app.include_router(production_router)
app.include_router(trading_router)

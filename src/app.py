from fastapi import FastAPI
from src.api import production_router
from src.dependencies import injector
from src.domain.interfaces import DBPopulatorService

print("Populating the database")
db_populator_service = injector.get(DBPopulatorService)
db_populator_service.populate()

print("Starting the application")
app = FastAPI()
app.include_router(production_router)

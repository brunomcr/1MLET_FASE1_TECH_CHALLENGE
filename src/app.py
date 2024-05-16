from fastapi import FastAPI
from src.api.routes import production_router
from src.services.dependencies import get_db_populator_service


db_populator_service = get_db_populator_service()
db_populator_service.populate()


app = FastAPI()
app.include_router(production_router)


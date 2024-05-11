from fastapi import APIRouter, Query
from src.services.get_production_data import ProductionDataService

production_router = APIRouter()

@production_router.get("/production", tags=["Production"])
async def get_data_production(ano: int = Query(default=None, description="Year: [1970-2022]")):
    '''Data on the production of wines, juices and estimates of the Rio Grande do Sul'''
    return ProductionDataService.get_production_data(ano)

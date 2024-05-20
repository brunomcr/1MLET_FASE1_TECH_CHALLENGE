from ..di import injector
from fastapi import APIRouter, HTTPException
from src.domain.interfaces import ProductionDataService
from src.domain.responses import GetProductionDataByYearResponse
import logging


logging.basicConfig(level=logging.INFO)

production_data_service = injector.get(ProductionDataService)
production_router = APIRouter()


@production_router.get("/production/{year}", response_model=None)
async def get_production_data_by_year(year: int) -> GetProductionDataByYearResponse:
    try:
        return await production_data_service.get_production_data_by_year(year)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

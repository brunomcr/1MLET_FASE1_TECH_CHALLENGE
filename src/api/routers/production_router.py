from ..di import injector
from fastapi import APIRouter, HTTPException
from src.domain.interfaces import ProductionService
from src.domain.responses.production import GetProductionByYearResponse
import logging


logging.basicConfig(level=logging.INFO)

production_service = injector.get(ProductionService)
production_router = APIRouter()


@production_router.get("/production/{year}", response_model=None)
async def get_production_by_year(year: int) -> GetProductionByYearResponse:
    try:
        return await production_service.get_production_by_year(year)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

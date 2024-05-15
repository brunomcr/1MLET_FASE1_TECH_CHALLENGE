from fastapi import APIRouter, HTTPException
from src.dependencies import get_production_service
from src.domain.responses.production.get_production_by_year_response import GetProductionByYearResponse
import logging

logging.basicConfig(level=logging.INFO)

production_service = get_production_service()
production_router = APIRouter()

@production_router.get("/production/{year}", response_model=None)
async def get_production_by_year(year: int) -> GetProductionByYearResponse:
    try:
        production_data = await production_service.get_production_by_year(year)
        if not production_data:
            raise HTTPException(status_code=404, detail="No data found for this year")
        return GetProductionByYearResponse(data=production_data)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter, HTTPException, Depends, Security
import logging

from ..di import injector
from ...domain.responses import GetProductionDataByYearResponse
from ...domain.interfaces.services import ProductionDataService
from ...services import JWTBearer

logging.basicConfig(level=logging.INFO)


def get_production_data_service() -> ProductionDataService:
    return injector.get(ProductionDataService)


production_router = APIRouter()


@production_router.get("/production/{year}",
                       response_model=GetProductionDataByYearResponse,
                       dependencies=[Security(JWTBearer())],
                       summary="Get production data by year",
                       description="Retrieve data on the production of wines, juices, and estimates in Rio Grande do Sul.",
                       tags=["Production Data"])
async def get_production_data_by_year(
        year: int,
        production_data_service: ProductionDataService = Depends(get_production_data_service)
) -> GetProductionDataByYearResponse:
    """
    Fetches the production data for a specific year.

    - **year**: Year for which the data is requested.
    """
    try:
        return await production_data_service.get_production_data_by_year(year)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

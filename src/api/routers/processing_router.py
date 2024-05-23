from fastapi import APIRouter, HTTPException, Security
import logging

from ..di import injector
from ...domain.interfaces.services import ProcessingDataService
from ...domain.responses import GetProcessingDataByYearResponse
from ...services import JWTBearer

logging.basicConfig(level=logging.INFO)

processing_data_service = injector.get(ProcessingDataService)
processing_router = APIRouter()


@processing_router.get("/processing/{year}",
    response_model=GetProcessingDataByYearResponse,
    dependencies=[Security(JWTBearer())],
    summary="Get processing data by year",
    description="Retrieve data on the quantity of grapes processed in Rio Grande do Sul.",
    tags=["Processing Data"]
)
async def get_processing_data_by_year(year: int) -> GetProcessingDataByYearResponse:
    """
    Fetches the processing data for a specific year.

    - **year**: Year for which the data is requested.
    """
    try:
        return await processing_data_service.get_processing_data_by_year(year)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

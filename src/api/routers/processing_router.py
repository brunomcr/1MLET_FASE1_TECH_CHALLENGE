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
                       dependencies=[Security(JWTBearer())])
async def get_processing_data_by_year(year: int) -> GetProcessingDataByYearResponse:
    try:
        return await processing_data_service.get_processing_data_by_year(year)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

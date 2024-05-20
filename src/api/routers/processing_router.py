from ..di import injector
from fastapi import APIRouter, HTTPException
from src.domain.responses import GetProcessingDataByYearResponse
import logging


logging.basicConfig(level=logging.INFO)

#processing_data_service = injector.get(ProcessingDataService)
processing_router = APIRouter()


@processing_router.get("/processing/{year}", response_model=None)
async def get_processing_data_by_year(year: int) -> GetProcessingDataByYearResponse:
    pass

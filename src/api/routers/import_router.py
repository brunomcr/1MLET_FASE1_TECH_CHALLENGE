from ..di import injector
from fastapi import APIRouter, HTTPException
from src.domain.interfaces import ImportDataService
from src.domain.responses import GetImportDataByYearResponse
import logging


logging.basicConfig(level=logging.INFO)

import_data_service = injector.get(ImportDataService)
import_router = APIRouter()


@import_router.get("/import/{year}", response_model=None)
async def get_import_data_by_year(year: int) -> GetImportDataByYearResponse:
    try:
        return await import_data_service.get_import_data_by_year(year)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

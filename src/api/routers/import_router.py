from fastapi import APIRouter, HTTPException, Security
import logging

from ..di import injector
from ...domain.interfaces.services import ImportDataService
from ...domain.responses import GetImportDataByYearResponse
from ...services import JWTBearer

logging.basicConfig(level=logging.INFO)

import_data_service = injector.get(ImportDataService)
import_router = APIRouter()


@import_router.get("/import/{year}",
    response_model=GetImportDataByYearResponse,
    dependencies=[Security(JWTBearer())],
    summary="Get import data by year",
    description="Retrieve data on the import of grape derivatives.",
    tags=["Import Data"]
)
async def get_import_data_by_year(year: int) -> GetImportDataByYearResponse:
    """
    Fetches the import data for a specific year.

    - **year**: Year for which the data is requested.
    """
    try:
        return await import_data_service.get_import_data_by_year(year)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

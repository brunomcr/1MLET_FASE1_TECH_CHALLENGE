from fastapi import APIRouter, HTTPException, Security
import logging

from ..di import injector
from ...domain.interfaces.services import ExportDataService
from ...domain.responses import GetExportDataByYearResponse
from ...services import JWTBearer

logging.basicConfig(level=logging.INFO)

export_data_service = injector.get(ExportDataService)
export_router = APIRouter()


@export_router.get("/export/{year}",
    response_model=GetExportDataByYearResponse,
    dependencies=[Security(JWTBearer())],
    summary="Get export data by year",
    description="Retrieve data on the export of grape derivatives.",
    tags=["Export Data"]
)
async def get_export_data_by_year(year: int) -> GetExportDataByYearResponse:
    """
    Fetches the export data for a specific year.

    - **year**: Year for which the data is requested.
    """
    try:
        return await export_data_service.get_export_data_by_year(year)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

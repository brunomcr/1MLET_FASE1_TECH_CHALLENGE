from fastapi import APIRouter, HTTPException, Security
import logging

from ..di import injector
from ...domain.responses import GetExportDataByYearResponse
from ...services import JWTBearer

logging.basicConfig(level=logging.INFO)

#export_service = injector.get(ExportService)
export_router = APIRouter()


@export_router.get("/export/{year}",
                   response_model=GetExportDataByYearResponse,
                   dependencies=[Security(JWTBearer())])
async def get_export_by_year(year: int) -> GetExportDataByYearResponse:
    pass

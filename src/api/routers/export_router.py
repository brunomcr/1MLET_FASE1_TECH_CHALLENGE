from ..di import injector
from fastapi import APIRouter, HTTPException
from src.domain.responses import GetExportDataByYearResponse
import logging


logging.basicConfig(level=logging.INFO)

#export_service = injector.get(ExportService)
export_router = APIRouter()


@export_router.get("/export/{year}", response_model=None)
async def get_export_by_year(year: int) -> GetExportDataByYearResponse:
    pass

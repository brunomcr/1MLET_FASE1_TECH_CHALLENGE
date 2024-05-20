from ..di import injector
from fastapi import APIRouter, HTTPException
from src.domain.responses import GetImportDataByYearResponse
import logging


logging.basicConfig(level=logging.INFO)

#import_service = injector.get(ImportService)
import_router = APIRouter()


@import_router.get("/import/{year}", response_model=None)
async def get_import_by_year(year: int) -> GetImportDataByYearResponse:
    pass

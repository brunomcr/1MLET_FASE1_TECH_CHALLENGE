from fastapi import APIRouter, Query
from src.services.get_export_data import ExportDataService

export_router = APIRouter()

@export_router.get("/export", tags=["Export"])
async def get_exportacao(
    product: str = Query(..., description='''Choose one of the options below:\n
    1) Table wines
    2) Sparkling wines
    3) Fresh Grapes
    4) Grape Juice'''),
    ano: int = Query(default=None, description="Year: [1970-2022]")):
    '''Data on the export of grape derivatives'''
    return ExportDataService.get_export_data(product, ano)


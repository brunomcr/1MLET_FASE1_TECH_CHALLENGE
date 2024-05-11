from fastapi import APIRouter, Query
from src.services.get_import_data import ImportDataService

import_router = APIRouter()

@import_router.get("/import", tags=["Import"])
async def get_importacao(
    product: str = Query(..., description='''Choose one of the options below:\n
    1) Table Wines
    2) Sparkling wines
    3) Fresh Grapes
    4) Raisins
    5) Grape Juice'''),
    ano: int = Query(default=None, description="Year: [1970-2022]")):
    '''Data on the import of grape derivatives'''
    return ImportDataService.get_import_data(product, ano)

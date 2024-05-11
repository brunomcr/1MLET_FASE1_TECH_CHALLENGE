from fastapi import APIRouter, Query
from src.services.get_processing_data import ProcessingDataService

processing_router = APIRouter()

@processing_router.get("/processing", tags=["Processing"])
async def get_data_processing(
    product: str = Query(..., description='''Choose one of the options below:\n
    1) Viniferas
    2) American and Hybrids
    3) Table Grapes
    4) No Classification'''),
    ano: int = Query(default=None, description="Year: [1970-2022]")):
    '''Data on the quantity of grapes Processed in Rio Grande do Sul'''
    return ProcessingDataService.get_processing_data(product, ano)

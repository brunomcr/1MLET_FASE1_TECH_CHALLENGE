from fastapi import APIRouter, Query
from src.services.get_trade_data import TradeDataService

trade_router = APIRouter()

@trade_router.get("/trade", tags=["Trade"])
async def get_data_trade(ano: int = Query(default=None, description="Year: [1970-2022]")):
    '''Data on the commercialization of wines and derivatives in Rio Grande do Sul'''
    return TradeDataService.get_trade_data(ano)

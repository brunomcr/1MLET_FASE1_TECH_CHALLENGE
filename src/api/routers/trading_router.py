from ..di import injector
from fastapi import APIRouter, HTTPException
from src.domain.responses import GetTradingDataByYearResponse
import logging


logging.basicConfig(level=logging.INFO)

#trading_data_service = injector.get(ProductionService)
trading_router = APIRouter()


@trading_router.get("/trading/{year}", response_model=None)
async def get_trading_data_by_year(year: int) -> GetTradingDataByYearResponse:
    pass

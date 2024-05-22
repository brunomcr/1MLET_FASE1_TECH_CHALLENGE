from fastapi import APIRouter, HTTPException, Security
import logging

from ..di import injector
from ...domain.responses import GetTradingDataByYearResponse
from ...services import JWTBearer

logging.basicConfig(level=logging.INFO)

#trading_data_service = injector.get(ProductionService)
trading_router = APIRouter()


@trading_router.get("/trading/{year}",
                    response_model=GetTradingDataByYearResponse,
                    dependencies=[Security(JWTBearer())])
async def get_trading_data_by_year(year: int) -> GetTradingDataByYearResponse:
    pass

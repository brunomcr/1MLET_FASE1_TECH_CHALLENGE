from typing import List
from pydantic import BaseModel

from ..models import TradingData


class GetTradingDataByYearResponse(BaseModel):
    data: List[TradingData]

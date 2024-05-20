from typing import List
from src.domain.models import TradingData


class GetTradingDataByYearResponse:
    def __init__(self, data: List[TradingData]):
        self.data = data

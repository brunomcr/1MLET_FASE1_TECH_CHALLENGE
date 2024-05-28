from abc import ABC, abstractmethod
from typing import List
from src.domain.models import TradingData


class TradingnDataRepository(ABC):
    @abstractmethod
    async def get_trading_data_by_year(self, year: int) -> List[TradingData]:
        raise NotImplementedError

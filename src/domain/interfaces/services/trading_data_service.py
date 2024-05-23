from abc import ABC, abstractmethod
from src.domain.responses import GetTradingDataByYearResponse


class TradingDataService(ABC):
    @abstractmethod
    async def get_trading_data_by_year(self, year: int) -> GetTradingDataByYearResponse:
        raise NotImplementedError

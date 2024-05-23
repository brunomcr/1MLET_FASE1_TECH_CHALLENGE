from .interfaces import TradingnDataRepository
from ..domain.interfaces.services import TradingDataService
from ..domain.responses import GetTradingDataByYearResponse
from ..services.di.dependencies import injector


class TradingDataServiceImpl(TradingDataService):
    def __init__(self):
        self.trading_repository = injector.get(TradingnDataRepository)

    async def get_trading_data_by_year(self, year: int) -> GetTradingDataByYearResponse:
        trading_data = await self.trading_repository.get_trading_data_by_year(year)
        return GetTradingDataByYearResponse(data=trading_data)

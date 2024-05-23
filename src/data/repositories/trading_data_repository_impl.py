from fastapi import HTTPException
from typing import List

from ..constants import COL_YEAR
from ..di.dependencies import injector
from ..interfaces import DatabaseHelper
from ...domain.models import TradingData
from ...services.interfaces import TradingnDataRepository

import logging


logging.basicConfig(level=logging.INFO)


class TradingDataRepositoryImpl(TradingnDataRepository):

    def __init__(self):
        self.database = injector.get(DatabaseHelper)

    async def get_trading_data_by_year(self, year: int) -> List[TradingData]:
        try:
            logging.info(f"Querying Trading data for year: {year}")
            query_result = self.database.find("trade", {COL_YEAR: str(year)})
            return [TradingData(**item) for item in query_result]
        except Exception as e:
            logging.error(f"Error querying MongoDB: {e}")
            raise HTTPException(status_code=500, detail=str(e))

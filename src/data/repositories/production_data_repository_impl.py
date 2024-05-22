from fastapi import HTTPException
from typing import List

from ..mappers import ProductionDataMapper
from ..di.dependencies import injector
from ..interfaces import DatabaseHelper
from ...domain.models import ProductionData
from ...services.interfaces import ProductionDataRepository

import logging


logging.basicConfig(level=logging.INFO)


class ProductionDataRepositoryImpl(ProductionDataRepository):

    def __init__(self):
        self.database = injector.get(DatabaseHelper)
        self.mapper = ProductionDataMapper()

    async def get_production_data_by_year(self, year: int) -> List[ProductionData]:
        try:
            logging.info(f"Querying Production data for year: {year}")
            
            query_result = self.database.find("production", {"Ano": str(year)})
            production_list = self.mapper.map(query_result)

            logging.debug(f"Mapped production data: {production_list}")

            return production_list
        except Exception as e:
            logging.error(f"Error querying MongoDB: {e}")
            raise HTTPException(status_code=500, detail=str(e))

from fastapi import HTTPException
from typing import List

from src.data.mappers import ProcessingDataMapper
from src.domain.models import ProcessingData
from src.services.interfaces import ProcessingDataRepository
from src.data.di.dependencies import injector
from src.data.interfaces import DatabaseHelper

import logging


logging.basicConfig(level=logging.INFO)


class ProcessingDataRepositoryImpl(ProcessingDataRepository):

    def __init__(self):
        self.database = injector.get(DatabaseHelper)
        self.mapper = ProcessingDataMapper()

    async def get_processing_data_by_year(self, year: int) -> List[ProcessingData]:
        try:
            logging.info(f"Querying Processing data for year: {year}")
            
            query_result = self.database.find("processing", {"Ano": str(year)})
            processing_list = self.mapper.map(query_result)

            logging.debug(f"Mapped processing data: {processing_list}")

            return processing_list
        except Exception as e:
            logging.error(f"Error querying MongoDB: {e}")
            raise HTTPException(status_code=500, detail=str(e))

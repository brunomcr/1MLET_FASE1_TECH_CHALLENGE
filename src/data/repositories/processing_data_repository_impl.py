import logging
from fastapi import HTTPException
from typing import List

from ..di.dependencies import injector
from ..interfaces import DatabaseHelper
from ..mappers import ProcessingDataMapper
from ...domain.models import ProcessingData
from ...services.interfaces import ProcessingDataRepository


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

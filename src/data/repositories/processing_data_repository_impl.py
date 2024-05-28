import logging
from fastapi import HTTPException
from typing import List

from ..constants import COL_YEAR
from ..di.dependencies import injector
from ..interfaces import DatabaseHelper
from ...domain.models import ProcessingData
from ...services.interfaces import ProcessingDataRepository


logging.basicConfig(level=logging.INFO)


class ProcessingDataRepositoryImpl(ProcessingDataRepository):

    def __init__(self):
        self.database = injector.get(DatabaseHelper)

    async def get_processing_data_by_year(self, year: int) -> List[ProcessingData]:
        try:
            logging.info(f"Querying Processing data for year: {year}")
            query_result = self.database.find("_processing", {COL_YEAR: str(year)})
            return [ProcessingData(**item) for item in query_result]
        except Exception as e:
            logging.error(f"Error querying MongoDB: {e}")
            raise HTTPException(status_code=500, detail=str(e))

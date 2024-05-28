from fastapi import HTTPException
from typing import List

from ..constants import COL_YEAR
from ..di.dependencies import injector
from ..interfaces import DatabaseHelper
from ...domain.models import ExportData
from ...services.interfaces import ExportDataRepository

import logging


logging.basicConfig(level=logging.INFO)


class ExportDataRepositoryImpl(ExportDataRepository):

    def __init__(self):
        self.database = injector.get(DatabaseHelper)

    async def get_export_data_by_year(self, year: int) -> List[ExportData]:
        try:
            logging.info(f"Querying Export data for year: {year}")
            query_result = self.database.find("_export", {COL_YEAR: str(year)})
            return [ExportData(**item) for item in query_result]
        except Exception as e:
            logging.error(f"Error querying MongoDB: {e}")
            raise HTTPException(status_code=500, detail=str(e))

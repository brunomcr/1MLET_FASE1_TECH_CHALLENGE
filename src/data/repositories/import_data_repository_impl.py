from fastapi import HTTPException
from typing import List

from ..constants import COL_YEAR
from ..di.dependencies import injector
from ..interfaces import DatabaseHelper
from ...domain.models import ImportData
from ...services.interfaces import ImportDataRepository

import logging


logging.basicConfig(level=logging.INFO)


class ImportDataRepositoryImpl(ImportDataRepository):

    def __init__(self):
        self.database = injector.get(DatabaseHelper)

    async def get_import_data_by_year(self, year: int) -> List[ImportData]:
        try:
            logging.info(f"Querying Import data for year: {year}")
            query_result = self.database.find("_import", {COL_YEAR: str(year)})
            return [ImportData(**item) for item in query_result]
        except Exception as e:
            logging.error(f"Error querying MongoDB: {e}")
            raise HTTPException(status_code=500, detail=str(e))

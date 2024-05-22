from fastapi import HTTPException
from typing import List

from ..di.dependencies import injector
from ..interfaces import DatabaseHelper
from ..mappers import ImportDataMapper
from ...domain.models import ImportData
from ...services.interfaces import ImportDataRepository

import logging


logging.basicConfig(level=logging.INFO)


class ImportDataRepositoryImpl(ImportDataRepository):

    def __init__(self):
        self.database = injector.get(DatabaseHelper)
        self.mapper = ImportDataMapper()

    async def get_import_data_by_year(self, year: int) -> List[ImportData]:
        try:
            logging.info(f"Querying Import data for year: {year}")
            
            query_result = self.database.find("import", {"Ano": str(year)})
            import_list = self.mapper.map(query_result)

            logging.debug(f"Mapped import data: {import_list}")

            return import_list
        except Exception as e:
            logging.error(f"Error querying MongoDB: {e}")
            raise HTTPException(status_code=500, detail=str(e))

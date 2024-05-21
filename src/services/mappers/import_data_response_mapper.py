from typing import List
from src.domain.models.import_data import ImportData
from src.domain.responses import GetImportDataByYearResponse


class ImportDataResponseMapper:
    @staticmethod
    def map(import_data: List[ImportData]) -> GetImportDataByYearResponse:
        return GetImportDataByYearResponse(data=import_data)

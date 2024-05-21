from abc import ABC, abstractmethod
from src.domain.responses import GetImportDataByYearResponse


class ImportDataService(ABC):
    @abstractmethod
    async def get_import_data_by_year(self, year: int) -> GetImportDataByYearResponse:
        raise NotImplementedError

from abc import ABC, abstractmethod

from ....domain.responses import GetExportDataByYearResponse


class ExportDataService(ABC):
    @abstractmethod
    async def get_export_data_by_year(self, year: int) -> GetExportDataByYearResponse:
        raise NotImplementedError

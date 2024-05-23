from .interfaces import ExportDataRepository
from ..domain.interfaces.services import ExportDataService
from ..domain.responses import GetExportDataByYearResponse
from ..services.di.dependencies import injector


class ExportDataServiceImpl(ExportDataService):
    def __init__(self):
        self.export_repository = injector.get(ExportDataRepository)

    async def get_export_data_by_year(self, year: int) -> GetExportDataByYearResponse:
        export_data = await self.export_repository.get_export_data_by_year(year)
        return GetExportDataByYearResponse(data=export_data)

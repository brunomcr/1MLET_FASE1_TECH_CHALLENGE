from .interfaces import ImportDataRepository
from ..domain.interfaces.services import ImportDataService
from ..domain.responses import GetImportDataByYearResponse
from ..services.di.dependencies import injector


class ImportDataServiceImpl(ImportDataService):
    def __init__(self):
        self.import_repository = injector.get(ImportDataRepository)

    async def get_import_data_by_year(self, year: int) -> GetImportDataByYearResponse:
        import_data = await self.import_repository.get_import_data_by_year(year)
        return GetImportDataByYearResponse(data=import_data)

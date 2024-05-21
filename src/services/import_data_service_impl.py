from src.domain.interfaces import ImportDataService
from src.domain.responses import GetImportDataByYearResponse
from src.services.mappers import ImportDataResponseMapper
from .interfaces import ImportDataRepository
from src.services.di.dependencies import injector


class ImportDataServiceImpl(ImportDataService):
    def __init__(self):
        self.import_repository = injector.get(ImportDataRepository)
        self.mapper = ImportDataResponseMapper()

    async def get_import_data_by_year(self, year: int) -> GetImportDataByYearResponse:
        import_data = await self.import_repository.get_import_data_by_year(year)
        return self.mapper.map(import_data)

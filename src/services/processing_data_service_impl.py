from .interfaces import ProcessingDataRepository
from ..domain.interfaces.services import ProcessingDataService
from ..domain.responses import GetProcessingDataByYearResponse
from ..services.di.dependencies import injector


class ProcessingDataServiceImpl(ProcessingDataService):
    def __init__(self):
        self.processing_repository = injector.get(ProcessingDataRepository)

    async def get_processing_data_by_year(self, year: int) -> GetProcessingDataByYearResponse:
        processing_data = await self.processing_repository.get_processing_data_by_year(year)
        return GetProcessingDataByYearResponse(data=processing_data)

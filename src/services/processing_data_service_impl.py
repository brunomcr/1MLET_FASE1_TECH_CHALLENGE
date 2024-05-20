from src.domain.interfaces import ProcessingDataService
from src.domain.responses import GetProcessingDataByYearResponse
from src.services.mappers import ProcessingDataResponseMapper
from .interfaces import ProcessingDataRepository
from src.services.di.dependencies import injector


class ProcessingDataServiceImpl(ProcessingDataService):
    def __init__(self):
        self.processing_repository = injector.get(ProcessingDataRepository)
        self.mapper = ProcessingDataResponseMapper()

    async def get_processing_data_by_year(self, year: int) -> GetProcessingDataByYearResponse:
        processing_data = await self.processing_repository.get_processing_data_by_year(year)
        return self.mapper.map(processing_data)

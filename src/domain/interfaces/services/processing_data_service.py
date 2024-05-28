from abc import ABC, abstractmethod

from ....domain.responses import GetProcessingDataByYearResponse


class ProcessingDataService(ABC):
    @abstractmethod
    async def get_processing_data_by_year(self, year: int) -> GetProcessingDataByYearResponse:
        raise NotImplementedError

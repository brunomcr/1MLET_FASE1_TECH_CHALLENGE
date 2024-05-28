from abc import ABC, abstractmethod
from typing import List
from src.domain.models import ProcessingData


class ProcessingDataRepository(ABC):
    @abstractmethod
    async def get_processing_data_by_year(self, year: int) -> List[ProcessingData]:
        raise NotImplementedError

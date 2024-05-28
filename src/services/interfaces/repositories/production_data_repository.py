from abc import ABC, abstractmethod
from typing import List
from src.domain.models import ProductionData


class ProductionDataRepository(ABC):
    @abstractmethod
    async def get_production_data_by_year(self, year: int) -> List[ProductionData]:
        raise NotImplementedError

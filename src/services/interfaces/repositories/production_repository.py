from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Production


class ProductionRepository(ABC):
    @abstractmethod
    async def get_production_by_year(self, year: int) -> List[Production]:
        raise NotImplementedError

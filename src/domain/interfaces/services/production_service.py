from abc import ABC, abstractmethod
from src.domain.responses import GetProductionByYearResponse


class ProductionService(ABC):
    @abstractmethod
    async def get_production_by_year(self, year: int) -> GetProductionByYearResponse:
        raise NotImplementedError

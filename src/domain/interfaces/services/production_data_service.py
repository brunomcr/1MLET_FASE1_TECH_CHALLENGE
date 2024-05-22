from abc import ABC, abstractmethod

from ....domain.responses import GetProductionDataByYearResponse


class ProductionDataService(ABC):
    @abstractmethod
    async def get_production_data_by_year(self, year: int) -> GetProductionDataByYearResponse:
        raise NotImplementedError

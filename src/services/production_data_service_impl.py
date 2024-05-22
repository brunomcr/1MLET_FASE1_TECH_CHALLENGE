from .interfaces import ProductionDataRepository
from ..domain.interfaces.services import ProductionDataService
from ..domain.responses import GetProductionDataByYearResponse
from ..services.mappers import ProductionDataResponseMapper
from ..services.di.dependencies import injector


class ProductionDataServiceImpl(ProductionDataService):
    def __init__(self):
        self.production_repository = injector.get(ProductionDataRepository)
        self.mapper = ProductionDataResponseMapper()

    async def get_production_data_by_year(self, year: int) -> GetProductionDataByYearResponse:
        production_data = await self.production_repository.get_production_data_by_year(year)
        return self.mapper.map(production_data)

from src.domain.interfaces import ProductionDataService
from src.domain.responses import GetProductionDataByYearResponse
from src.services.mappers import ProductionDataResponseMapper
from .interfaces import ProductionDataRepository
from src.services.di.dependencies import injector


class ProductionDataServiceImpl(ProductionDataService):
    def __init__(self):
        self.production_repository = injector.get(ProductionDataRepository)
        self.mapper = ProductionDataResponseMapper()

    async def get_production_data_by_year(self, year: int) -> GetProductionDataByYearResponse:
        production_data = await self.production_repository.get_production_data_by_year(year)
        return self.mapper.map(production_data)

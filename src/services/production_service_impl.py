from src.domain.interfaces import ProductionService
from src.domain.responses import GetProductionByYearResponse
from src.services.mappers.production_response_mapper import ProductionResponseMapper
from .interfaces import ProductionRepository
from src.services.di.dependencies import injector


class ProductionServiceImpl(ProductionService):
    def __init__(self):
        self.production_repository = injector.get(ProductionRepository)
        self.mapper = ProductionResponseMapper()

    async def get_production_by_year(self, year: int) -> GetProductionByYearResponse:
        production_data = await self.production_repository.get_production_by_year(year)
        return self.mapper.map(production_data)

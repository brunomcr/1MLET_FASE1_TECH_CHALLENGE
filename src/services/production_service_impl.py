from src.domain.interfaces import ProductionService
from src.domain.responses import GetProductionByYearResponse
from src.services.mappers.production_response_mapper import ProductionResponseMapper
from src.data.repositories.production.production_repository_impl import ProductionRepositoryImpl

class ProductionServiceImpl(ProductionService):

    def __init__(self):
        self.production_repository = ProductionRepositoryImpl()
        self.mapper = ProductionResponseMapper()

    async def get_production_by_year(self, year: int) -> GetProductionByYearResponse:
        production_data = await self.production_repository.get_production_by_year(year)
        return self.mapper.map(production_data)

from src.domain.interfaces import ProductionService
from src.dependencies import get_production_repository
from src.domain.responses import GetProductionByYearResponse
from ..mappers import ProductionResponseMapper


class ProductionServiceImpl(ProductionService):

    def __init__(self):
        self.production_repository = get_production_repository()
        self.mapper = ProductionResponseMapper()

    async def get_production_by_year(self, year: int) -> GetProductionByYearResponse:
        production_data = await self.production_repository.get_production_by_year(year)
        return self.mapper.map(year, production_data)

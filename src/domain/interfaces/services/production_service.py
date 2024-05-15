from src.domain.responses import GetProductionByYearResponse


class ProductionService:
    async def get_production_by_year(self, year: int) -> GetProductionByYearResponse:
        raise NotImplementedError

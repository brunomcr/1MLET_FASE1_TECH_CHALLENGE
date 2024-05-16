from typing import List
from src.domain.models.production import Production
from src.domain.responses.production.get_production_by_year_response import GetProductionByYearResponse


class ProductionResponseMapper:
    @staticmethod
    def map(production_data: List[Production]) -> GetProductionByYearResponse:
        return GetProductionByYearResponse(data=production_data)

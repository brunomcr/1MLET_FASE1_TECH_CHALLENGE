from typing import List

from src.domain.models import Production
from src.domain.responses import GetProductionByYearResponse


class ProductionResponseMapper:

    @staticmethod
    def map(year: int, production_data: List[Production]) -> GetProductionByYearResponse:
        return GetProductionByYearResponse(year=year, data=production_data)

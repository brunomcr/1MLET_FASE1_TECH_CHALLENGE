from typing import List
from src.domain.models.production_data import ProductionData
from src.domain.responses import GetProductionDataByYearResponse


class ProductionDataResponseMapper:
    @staticmethod
    def map(production_data: List[ProductionData]) -> GetProductionDataByYearResponse:
        return GetProductionDataByYearResponse(data=production_data)

from typing import List
from src.domain.models import ProductionData


class GetProductionDataByYearResponse:
    def __init__(self, data: List[ProductionData]):
        self.data = data

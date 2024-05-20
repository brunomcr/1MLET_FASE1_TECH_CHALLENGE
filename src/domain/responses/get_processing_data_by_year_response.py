from typing import List
from src.domain.models import ProcessingData


class GetProcessingDataByYearResponse:
    def __init__(self, data: List[ProcessingData]):
        self.data = data

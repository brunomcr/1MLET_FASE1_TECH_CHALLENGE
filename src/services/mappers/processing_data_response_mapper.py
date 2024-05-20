from typing import List
from src.domain.models.processing_data import ProcessingData
from src.domain.responses import GetProcessingDataByYearResponse


class ProcessingDataResponseMapper:
    @staticmethod
    def map(processing_data: List[ProcessingData]) -> GetProcessingDataByYearResponse:
        return GetProcessingDataByYearResponse(data=processing_data)

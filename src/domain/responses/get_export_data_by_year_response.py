from typing import List
from src.domain.models import ExportData


class GetExportDataByYearResponse:
    def __init__(self, data: List[ExportData]):
        self.data = data

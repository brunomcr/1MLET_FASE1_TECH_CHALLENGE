from typing import List
from src.domain.models import ImportData


class GetImportDataByYearResponse:
    def __init__(self, data: List[ImportData]):
        self.data = data

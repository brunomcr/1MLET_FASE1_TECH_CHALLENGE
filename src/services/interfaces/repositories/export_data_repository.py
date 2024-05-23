from abc import ABC, abstractmethod
from typing import List
from src.domain.models import ExportData


class ExportDataRepository(ABC):
    @abstractmethod
    async def get_export_data_by_year(self, year: int) -> List[ExportData]:
        raise NotImplementedError

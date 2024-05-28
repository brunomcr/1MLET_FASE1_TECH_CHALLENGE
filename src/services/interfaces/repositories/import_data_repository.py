from abc import ABC, abstractmethod
from typing import List
from src.domain.models import ImportData


class ImportDataRepository(ABC):
    @abstractmethod
    async def get_import_data_by_year(self, year: int) -> List[ImportData]:
        raise NotImplementedError

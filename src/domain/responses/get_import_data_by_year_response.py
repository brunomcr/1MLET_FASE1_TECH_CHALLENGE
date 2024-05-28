from typing import List
from pydantic import BaseModel

from ..models import ImportData


class GetImportDataByYearResponse(BaseModel):
    data: List[ImportData]

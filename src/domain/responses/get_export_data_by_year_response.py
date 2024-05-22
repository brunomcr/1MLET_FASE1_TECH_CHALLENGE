from typing import List
from pydantic import BaseModel

from ..models import ExportData


class GetExportDataByYearResponse(BaseModel):
    data: List[ExportData]

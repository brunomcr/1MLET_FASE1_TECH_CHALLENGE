from typing import List
from pydantic import BaseModel

from ..models import ProductionData


class GetProductionDataByYearResponse(BaseModel):
    data: List[ProductionData]

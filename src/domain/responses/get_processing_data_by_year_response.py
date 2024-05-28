from typing import List
from pydantic import BaseModel

from ..models import ProcessingData


class GetProcessingDataByYearResponse(BaseModel):
    data: List[ProcessingData]

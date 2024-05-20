from typing import List
from ...models import Production


class GetProductionByYearResponse:
    def __init__(self, data: List[Production]):
        self.data = data

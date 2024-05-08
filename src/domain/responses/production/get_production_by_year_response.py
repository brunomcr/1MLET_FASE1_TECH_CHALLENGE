from typing import List

from ...models import Production


class GetProductionByYearResponse:
    def __init__(self, year: int, data: List[Production]):
        self.year = year
        self.data = data

from typing import List

from src.domain.models import Production
from src.services.interfaces import ProductionRepository
from ...helpers import read_json, JSON_DIR
from ...mappers import ProductionMapper


class ProductionRepositoryImpl(ProductionRepository):

    PRODUCTION_FILE = 'producao.json'

    def __init__(self):
        self.mapper = ProductionMapper()

    async def get_production_by_year(self, year: int) -> List[Production]:
        data = read_json(JSON_DIR + self.PRODUCTION_FILE)
        production_data = self.mapper.map(data)
        return [prod for prod in production_data if prod.year == str(year)]


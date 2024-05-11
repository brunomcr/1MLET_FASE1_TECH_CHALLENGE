from src.services.json_loader import JSONLoader
from src.models.data_options import DataOptions

class ImportDataService:
    @staticmethod
    def get_import_data(product_key: str, year: int):
        data = JSONLoader.get_json_file(DataOptions().import_, product_key)
        return JSONLoader.filter_data_by_year(data, year)

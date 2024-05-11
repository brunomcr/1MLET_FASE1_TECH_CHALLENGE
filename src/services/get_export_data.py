from src.services.json_loader import JSONLoader
from src.models.data_options import DataOptions

class ExportDataService:
    @staticmethod
    def get_export_data(product_key: str, year: int):
        data = JSONLoader.get_json_file(DataOptions().export, product_key)
        return JSONLoader.filter_data_by_year(data, year)

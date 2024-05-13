from src.services.json_loader import JSONLoader

class ProductionDataService:
    @staticmethod
    def get_production_data(year: int):
        data = JSONLoader.read_json('Producao.json')
        return JSONLoader.filter_data_by_year(data, year)

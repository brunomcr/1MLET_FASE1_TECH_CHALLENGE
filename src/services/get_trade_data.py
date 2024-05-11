from src.services.json_loader import JSONLoader

class TradeDataService:
    @staticmethod
    def get_trade_data(year: int):
        data = JSONLoader.read_json('Comercio.json')
        return JSONLoader.filter_data_by_year(data, year)

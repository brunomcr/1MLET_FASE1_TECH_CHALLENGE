import json
from fastapi import HTTPException
from pathlib import Path
from src.config import DATA_DIR

class JSONLoader:
    @staticmethod
    def read_json(file_name: str):
        file_path = Path(DATA_DIR) / file_name
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Error decoding JSON")

    @staticmethod
    def get_json_file(option_dict: dict, product_key: str):
        file_name = option_dict.get(product_key)
        if not file_name:
            raise HTTPException(status_code=400, detail="Invalid product option")
        return JSONLoader.read_json(file_name)

    @staticmethod
    def filter_data_by_year(data: list, year: int):
        return [item for item in data if int(item.get('Ano', 0)) == year]

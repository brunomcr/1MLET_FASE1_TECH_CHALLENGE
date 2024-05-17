from fastapi import HTTPException
from src.data.mappers import ProductionMapper
from src.domain.models import Production
from src.services.interfaces import ProductionRepository
from typing import List
from src.data.helpers.mongo_database_helper import MongoDatabaseHelper
import logging


logging.basicConfig(level=logging.INFO)


class ProductionRepositoryImpl(ProductionRepository):

    def __init__(self):
        self.mapper = ProductionMapper()
        self.mongo_helper = MongoDatabaseHelper()

    async def get_production_by_year(self, year: int) -> List[Production]:
        try:
            logging.info(f"Querying MongoDB for year: {year}")
            collection = self.mongo_helper._MongoDatabaseHelper__db_connection['production']
            query_result = collection.find({"Ano": str(year)})

            filtered_data = [item for item in query_result]
            if not filtered_data:
                raise HTTPException(status_code=404, detail="No data found for this year")
            production_list = self.mapper.map(filtered_data)
            logging.info(f"Mapped production data: {production_list}")
            return production_list
        except Exception as e:
            logging.error(f"Error querying MongoDB: {e}")
            raise HTTPException(status_code=500, detail=str(e))




# from fastapi import HTTPException
# from src.data.mappers import ProductionMapper
# from src.domain.models import Production
# from src.services.interfaces import ProductionRepository
# from typing import List
# import json
# import logging
# import os


# logging.basicConfig(level=logging.INFO)


# class ProductionRepositoryImpl(ProductionRepository):

#     def __init__(self, json_dir=None):
#         if json_dir is None:
#             #json_dir = '/home/santili/fiap/projetos/1MLET_FASE1_TECH_CHALLENGE/res/json/'
#             json_dir = os.path.abspath('res/json/')
#         self.json_file = os.path.join(json_dir, 'Producao.json')
#         self.mapper = ProductionMapper()
#         logging.info(f"JSON file path: {self.json_file}")

#     async def get_production_by_year(self, year: int) -> List[Production]:
#         try:
#             logging.info(f"Opening JSON file: {self.json_file}")
#             with open(self.json_file, 'r', encoding='utf-8') as file:
#                 all_data = json.load(file)
#             logging.info(f"Filtering data for year: {year}")
#             filtered_data = [item for item in all_data if item.get('Ano') == str(year)]
#             if not filtered_data:
#                 raise HTTPException(status_code=404, detail="No data found for this year")
#             production_list = self.mapper.map(filtered_data)
#             logging.info(f"Mapped production data: {production_list}")
#             return production_list
#         except FileNotFoundError:
#             logging.error(f"File not found: {self.json_file}")
#             raise HTTPException(status_code=404, detail="File not found")
#         except json.JSONDecodeError:
#             logging.error(f"Error decoding JSON from file: {self.json_file}")
#             raise HTTPException(status_code=400, detail="Error decoding JSON")


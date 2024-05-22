import json
import os

from .di import injector
from ..data.constants import *
from ..data.interfaces import DatabaseHelper
from ..domain.interfaces.services import DBPopulatorService


class DBPopulatorServiceImpl(DBPopulatorService):
    def __init__(self):
        self.__db = injector.get(DatabaseHelper)

    def populate(self):
        json_directory = os.path.abspath('res/json/')

        field_mapping = {
            'Ano': COL_YEAR,
            'Pais': COL_COUNTRY,
            'Valor': COL_VALUE,
            'Grupo': COL_GROUP,
            'Produto': COL_PRODUCT,
            'Quantidade': COL_QUANTITY,
            'QuantidadeKg': COL_WEIGHT,
            'QuantidadeL': COL_VOLUME,
            'Cultivar': COL_CULTIVATION
        }

        # Mapping files to collections and product types
        file_mapping = {
            'Comercio.json': ('trade', None),
            'Producao.json': ('production', None),
            'ExpEspumantes.json': ('export', 'Espumantes'),
            'ExpSuco.json': ('export', 'Suco de uva'),
            'ExpUva.json': ('export', 'Uvas frescas'),
            'ExpVinho.json': ('export', 'Vinhos de mesa'),
            'ImpEspumantes.json': ('import', 'Espumantes'),
            'ImpFrescas.json': ('import', 'Uvas frescas'),
            'ImpPassas.json': ('import', 'Uvas passas'),
            'ImpSuco.json': ('import', 'Suco de uva'),
            'ImpVinhos.json': ('import', 'Vinhos de mesa'),
            'ProcessaAmericanas.json': ('processing', 'Americanas e hibridas'),
            'ProcessaMesa.json': ('processing', 'Uvas de mesa'),
            'ProcessaSemclass.json': ('processing', 'Sem classificação'),
            'ProcessaViniferas.json': ('processing', 'Viniferas')
        }

        for file, (collection_name, product_type) in file_mapping.items():
            file_path = os.path.join(json_directory, file)
            
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

                converted_data = []
                for entry in data:
                    converted_entry = {field_mapping.get(key, key): value for key, value in entry.items()}
                    if product_type:
                        converted_entry[COL_TYPE] = product_type
                    converted_data.append(converted_entry)

                self.__db.insert_many(collection_name, converted_data)
        print("Data loaded successfully!")

from .di import injector
from src.data.interfaces import DatabaseHelper
from src.domain.interfaces import DBPopulatorService
import json
import os


class DBPopulatorServiceImpl(DBPopulatorService):
    def __init__(self):
        self.__db = injector.get(DatabaseHelper)

    def populate(self):
        json_directory = os.path.abspath('res/json/')

        # Mapping files to collections and product types
        file_mapping = {
            'Comercio.json': ('comercio', None),
            'Producao.json': ('producao', None),
            'ExpEspumantes.json': ('exportacao', 'Espumantes'),
            'ExpSuco.json': ('exportacao', 'Suco de uva'),
            'ExpUva.json': ('exportacao', 'Uvas frescas'),
            'ExpVinho.json': ('exportacao', 'Vinhos de mesa'),
            'ImpEspumantes.json': ('importacao', 'Espumantes'),
            'ImpFrescas.json': ('importacao', 'Uvas frescas'),
            'ImpPassas.json': ('importacao', 'Uvas passas'),
            'ImpSuco.json': ('importacao', 'Suco de uva'),
            'ImpVinhos.json': ('importacao', 'Vinhos de mesa'),
            'ProcessaAmericanas.json': ('processamento', 'Americanas e hibridas'),
            'ProcessaMesa.json': ('processamento', 'Uvas de mesa'),
            'ProcessaSemclass.json': ('processamento', 'Sem classificação'),
            'ProcessaViniferas.json': ('processamento', 'Viniferas')
        }

        for file, (collection_name, product_type) in file_mapping.items():
            file_path = os.path.join(json_directory, file)
            
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                
                if product_type:
                    for entry in data:
                        entry['Produto'] = product_type
                self.__db.insert_many(collection_name, data)

        print("Data loaded successfully!")

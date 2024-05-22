import json
import os

from .di import injector
from ..data.interfaces import DatabaseHelper
from ..domain.interfaces.services import DBPopulatorService


class DBPopulatorServiceImpl(DBPopulatorService):
    def __init__(self):
        self.__db = injector.get(DatabaseHelper)

    def populate(self):
        json_directory = os.path.abspath('res/json/')

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
                
                if product_type:
                    for entry in data:
                        entry['Produto'] = product_type
                self.__db.insert_many(collection_name, data)

        print("Data loaded successfully!")

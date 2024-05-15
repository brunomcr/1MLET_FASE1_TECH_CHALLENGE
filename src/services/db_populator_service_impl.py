from src.domain.interfaces import DBPopulatorService
from src.dependencies import get_database_connection
import json
import os


class DBPopulatorServiceImpl(DBPopulatorService):

    def populate(self):
        db = get_database_connection()

        json_directory = '/res/json'

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
                db[collection_name].insert_many(data)

        print("Data loaded successfully!")

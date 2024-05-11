from pydantic import BaseModel

class DataOptions(BaseModel):
    processing: dict = {
        "1": "ProcessaViniferas.json", 
        "2": "ProcessaAmericanas.json", 
        "3": "ProcessaMesa.json", 
        "4": "ProcessaSemclass.json"
    }
    import_: dict = {
        "1": "ImpVinhos.json", 
        "2": "ImpEspumantes.json", 
        "3": "ImpFrescas.json", 
        "4": "ImpPassas.json", 
        "5": "ImpSuco.json"
    }
    export: dict = {
        "1": "ExpVinho.json", 
        "2": "ExpEspumantes.json", 
        "3": "ExpUva.json", 
        "4": "ExpSuco.json"
    }

    class Config:
        #allow_mutation = False
        extra = "forbid"  # Adicionando configuração recomendada para proibir campos extras

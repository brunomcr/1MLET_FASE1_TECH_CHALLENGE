from fastapi import FastAPI, HTTPException, Query
import json


dir_json = "cargas/json_files/"

app = FastAPI()


def read_json(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Error decoding JSON")


def filter_data_by_year(data, year):
    try:
        year = int(year)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid year format")
    return [item for item in data if int(item.get('Ano', 0)) == year]


file_mapping = {
    ("producao", "producao"): "Producao.json",
    ("processamento", "viniferas"): "ProcessaViniferas.json",
    ("processamento", "americanas_hibridas"): "ProcessaAmericanas.json",
    ("processamento", "uvas_mesa"): "ProcessaMesa.json",
    ("processamento", "sem_classificacao"): "ProcessaSemclass.json",
    ("comercio", "comercio"): "Comercio.json",
    ("importacao", "vinho_mesa"): "ImpVinhos.json",
    ("importacao", "espumantes"): "ImpEspumantes.json",
    ("importacao", "uvas_frescas"): "ImpFrescas.json",
    ("importacao", "uvas_passas"): "ImpPassas.json",
    ("importacao", "suco_uva"): "ImpSuco.json",
    ("exportacao", "vinho_mesa"): "ExpVinho.json",
    ("exportacao", "espumantes"): "ExpEspumantes.json",
    ("exportacao", "uvas_frescas"): "ExpUva.json",
    ("exportacao", "suco_uva"): "ExpSuco.json",
}

@app.get("/")
async def root():
    return {"message": "Hello 1MLET - Grupo 43"}

    
@app.get("/data")
def get_data(tab: str = Query(..., description="Escolha o tipo de dados que deseja buscar: \n" 
                              "ascascascasc"), 
             guia: str = Query(..., description="Escolha o guia, como 'uva', 'suco', etc."),
             year: int = Query(None, description="Ano para filtrar")):
    file_name = file_mapping.get((tab.lower(), guia.lower()))
    if not file_name:
        raise HTTPException(status_code=400, detail="Invalid tab/guia combination")

    data = read_json(dir_json+file_name)

    if year is not None:
        data = filter_data_by_year(data, year)

    return data





# file_mapping = {
#     "viniferas": "ProcessaViniferas.json",
#     "AmericanasHibridas": "ProcessaAmericanas.json",
#     "UvasMesa": "ProcessaMesa.json",
#     "SemClassificacao": "ProcessaSemclass.json"
# }


# @app.get("/producao")
# def get_data_comercio(Ano: int = Query(None, description="Insira o ano que deseja buscar")):
#     data = read_json(dir_json+'producao.json')
#     if Ano is not None:
#         data = filter_data_by_year(data, Ano)
#     return data


# @app.get("/processamento")
# def get_data_processamento(year: int = Query(None, description="Ano para filtrar"),
#               file_choice: str = Query(..., description="Escolha o dataset que deseja baixar")):
#     file_name = file_mapping.get(file_choice.lower())
#     if not file_name:
#         raise HTTPException(status_code=400, detail="Invalid file choice")

#     data = read_json(dir_json+file_name)
#     if year is not None:
#         data = filter_data_by_year(data, year)
#     return data


# @app.get("/comercio")
# def get_data_comercio(Ano: int = Query(None, description="Insira o ano que deseja buscar")):
#     data = read_json(dir_json+'Comercio.json')
#     if Ano is not None:
#         data = filter_data_by_year(data, Ano)
#     return data
from fastapi import FastAPI, HTTPException, Query
import json

app = FastAPI()

dir_json = "cargas/json_files/"

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



opcoes_processamento = {
    "1": "ProcessaViniferas.json",
    "2": "ProcessaAmericanas.json",
    "3": "ProcessaMesa.json",
    "4": "ProcessaSemclass.json"
}

@app.get("/")
async def root():
    return {"message": "Hello 1MLET - Grupo 43"}


@app.get("/producao")
def get_data_comercio(Ano: int = Query(None, description="Ano: [1970-2022]")):
    data = read_json(dir_json+'producao.json')
    if Ano is not None:
        data = filter_data_by_year(data, Ano)
    return data


@app.get("/processamento")
def get_processamento(Produto: str = Query(..., description='''Escolha as opções abaixo: \n
            1) Viniferas 
            2) Americanas e Hibridas 
            3) Uvas de Mesa 
            4) Sem Classificação'''),
             Ano: int = Query(None, description="Ano: [1970-2022]")):
    '''Comentario sobre o endpoint.......'''
    file_name = opcoes_processamento.get((Produto.lower()))
    if not file_name:
        raise HTTPException(status_code=400, detail="Opção Inválida")

    data = read_json(dir_json+file_name)

    if Ano is not None:
        data = filter_data_by_year(data, Ano)

    return data

@app.get("/comercio")
def get_data_comercio(Ano: int = Query(None, description="Ano: [1970-2022]")):
    data = read_json(dir_json+'Comercio.json')
    if Ano is not None:
        data = filter_data_by_year(data, Ano)
    return data


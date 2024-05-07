from concurrent.futures import ThreadPoolExecutor, as_completed
from functions_carga import get_data

_START_DATE = 1970
_LAST_DATE = 2024

# Opt e Subopt de cada pagina e o nome do arquivo.
tasks = [
    ('opt_04', None, 'Comercio.json'),
    ('opt_06', 'subopt_02', 'ExpEspumantes.json'),
    ('opt_06', 'subopt_04', 'ExpSuco.json'),
    ('opt_06', 'subopt_03', 'ExpUva.json'),
    ('opt_06', 'subopt_01', 'ExpVinho.json'),
    ('opt_05', 'subopt_02', 'ImpEspumantes.json'),
    ('opt_05', 'subopt_03', 'ImpFrescas.json'),
    ('opt_05', 'subopt_04', 'ImpPassas.json'),
    ('opt_05', 'subopt_05', 'ImpSuco.json'),
    ('opt_05', 'subopt_01', 'ImpVinhos.json'),
    ('opt_03', 'subopt_02', 'ProcessaAmericanas.json'),
    ('opt_03', 'subopt_03', 'ProcessaMesa.json'),
    ('opt_03', 'subopt_04', 'ProcessaSemclass.json'),
    ('opt_03', 'subopt_01', 'ProcessaViniferas.json'),
    ('opt_02', None, 'Producao.json')
]


# Função para executar get_data
def execute_get_data(option, suboption, filename):
    return get_data(option, suboption, filename, _START_DATE, _LAST_DATE)


# ThreadPoolExecutor para executar as tarefas em paralelo
with ThreadPoolExecutor() as executor:
    # Dicionário para armazenar futures
    future_to_task = {executor.submit(execute_get_data, *task): task for task in tasks}

    for future in as_completed(future_to_task):
        task = future_to_task[future]
        try:
            data = future.result()
        except Exception as exc:
            print(f"Task {task} generated an exception: {exc}")

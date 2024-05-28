from concurrent.futures import ThreadPoolExecutor, as_completed
from .web_scrapper import get_data

# Global variables to define start and end dates
_START_DATE = 1970
_LAST_DATE = 2024

# Tasks to be performed by page (option), subpage (suboption), and filename
tasks = [
    ('opt_02', None, 'Producao.json'),
    ('opt_03', 'subopt_01', 'ProcessaViniferas.json'),
    ('opt_03', 'subopt_02', 'ProcessaAmericanas.json'),
    ('opt_03', 'subopt_03', 'ProcessaMesa.json'),
    ('opt_03', 'subopt_04', 'ProcessaSemclass.json'),
    ('opt_04', None, 'Comercio.json'),
    ('opt_05', 'subopt_01', 'ImpVinhos.json'),
    ('opt_05', 'subopt_02', 'ImpEspumantes.json'),
    ('opt_05', 'subopt_03', 'ImpFrescas.json'),
    ('opt_05', 'subopt_04', 'ImpPassas.json'),
    ('opt_05', 'subopt_05', 'ImpSuco.json'),
    ('opt_06', 'subopt_01', 'ExpVinho.json'),
    ('opt_06', 'subopt_02', 'ExpEspumantes.json'),
    ('opt_06', 'subopt_04', 'ExpSuco.json'),
    ('opt_06', 'subopt_03', 'ExpUva.json')
]


# Function to execute the get_data function from the functions_carga module for each task
def execute_get_data(option, suboption, filename):
    return get_data(option, suboption, filename, _START_DATE, _LAST_DATE)


def async_get_data() -> None:
    # Using ThreadPoolExecutor to perform the execution in parallel
    with ThreadPoolExecutor() as executor:
        # Create a mapping of future tasks to their corresponding task details
        future_to_task = {executor.submit(execute_get_data, *task): task for task in tasks}

        # Iterate over completed tasks as they finish and handle exceptions
        for future in as_completed(future_to_task):
            task = future_to_task[future]
            try:
                data = future.result()  # Attempt to get the result of the future task
            except Exception as exc:  # Catch and handle exceptions
                print(f"Task {task} generated an exception: {exc}")


if __name__ == "__main__":
    async_get_data()

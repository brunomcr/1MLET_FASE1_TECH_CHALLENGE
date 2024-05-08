from concurrent.futures import ThreadPoolExecutor, as_completed
from functions_carga import get_data

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




# import argparse
# from datetime import datetime

# def main():
#     parser = argparse.ArgumentParser(description='Execute get_data function with given parameters.')
#     parser.add_argument('--option', type=str, help='Option parameter for get_data')
#     parser.add_argument('--suboption', type=str, default=None, help='Suboption parameter for get_data (optional)')
#     parser.add_argument('--filename', type=str, help='Filename parameter for get_data')
#     parser.add_argument('--start_date', type=int, default=1970, help='Start date for data fetching')
#     parser.add_argument('--end_date', type=int, default=datetime.now().year, help='End date for data fetching')


#     args = parser.parse_args()

#     result = get_data(args.option, args.suboption, args.filename, args.start_date, args.end_date)

# if __name__ == "__main__":
#     main()




# '''
# python cargas/parallel_web_scraper.py --option=opt_02 --filename=Producao.json &
# python cargas/parallel_web_scraper.py --option=opt_04 --filename=Comercio.json &
# python cargas/parallel_web_scraper.py --option=opt_06 --suboption=subopt_02 --filename=ExpEspumantes.json &
# python cargas/parallel_web_scraper.py --option=opt_06 --suboption=subopt_04 --filename=ExpSuco.json &
# python cargas/parallel_web_scraper.py --option=opt_06 --suboption=subopt_03 --filename=ExpUva.json &
# python cargas/parallel_web_scraper.py --option=opt_06 --suboption=subopt_01 --filename=ExpVinho.json &
# python cargas/parallel_web_scraper.py --option=opt_05 --suboption=subopt_02 --filename=ImpEspumantes.json &
# python cargas/parallel_web_scraper.py --option=opt_05 --suboption=subopt_03 --filename=ImpFrescas.json &
# python cargas/parallel_web_scraper.py --option=opt_05 --suboption=subopt_04 --filename=ImpPassas.json &
# python cargas/parallel_web_scraper.py --option=opt_05 --suboption=subopt_05 --filename=ImpSuco.json &
# python cargas/parallel_web_scraper.py --option=opt_05 --suboption=subopt_01 --filename=ImpVinhos.json &
# python cargas/parallel_web_scraper.py --option=opt_03 --suboption=subopt_02 --filename=ProcessaAmericanas.json &
# python cargas/parallel_web_scraper.py --option=opt_03 --suboption=subopt_03 --filename=ProcessaMesa.json &
# python cargas/parallel_web_scraper.py --option=opt_03 --suboption=subopt_04 --filename=ProcessaSemclass.json &
# python cargas/parallel_web_scraper.py --option=opt_03 --suboption=subopt_01 --filename=ProcessaViniferas.json &
# '''

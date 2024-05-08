import requests
from bs4 import BeautifulSoup
import json
import os

# URL base
base_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php'

# Json files directory
json_files_dir = 'cargas/json_files/'
if not os.path.exists(json_files_dir):
    os.mkdir(json_files_dir)


def get_data(opt, subopt, file_name, start_year, end_year):
    if opt == 'opt_05' and subopt in ('subopt_01', 'subopt_02', 'subopt_03', 'subopt_04', 'subopt_05') \
    or opt == 'opt_06' and subopt in ('subopt_01', 'subopt_02', 'subopt_03', 'subopt_04'): 
        opt_subopt_files = {
        (opt, subopt): file_name,
        }

        for (opt, subopt), files in opt_subopt_files.items():
            all_data = []  

            for year in range(start_year, end_year):
                params = {
                    'ano': year,
                    'opcao': opt,
                    'subopcao': subopt
                }
                
                response = requests.get(base_url, params=params, timeout=10000)
                soup = BeautifulSoup(response.text, 'html.parser')

                table = soup.find('table', class_='tb_base tb_dados')

                if table:
                    lines = table.find_all('tr')[1:] 
                    
                    for lines in lines[:-1]:
                        coluns = lines.find_all('td')
                        data_lines = {
                            "Ano": str(year),
                            "Pais": coluns[0].text.strip(),
                            "Quantidade": coluns[1].text.strip().replace("-", "0"),
                            "Valor": coluns[2].text.strip().replace("-", "0")
                        }
                        if data_lines["Pais"]:
                            all_data.append(data_lines)
            
            with open(json_files_dir + files, 'w', encoding='utf-8') as json_file:
                json.dump(all_data, json_file, ensure_ascii=False, indent=4)

            print(f"{files} file was created successfully!")
    
    elif opt == 'opt_02' and subopt == None \
    or opt == 'opt_04' and subopt == None:
        all_data = []  

        for year in range(start_year, end_year):
            params = {
                'ano': year,
                'opcao': opt,
                'subopcao': subopt
            }
            
            response = requests.get(base_url, params=params, timeout=10000)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            table = soup.find('table', class_='tb_base tb_dados')

            if table:
                current_group = ""  

                for lines in table.find_all('tr'):
                    item = lines.find('td', class_='tb_item')
                    subitem = lines.find('td', class_='tb_subitem')

                    if item:
                        current_group = item.text.strip()
                    
                    if subitem and current_group: 
                        product = subitem.text.strip()
                        volume = subitem.find_next_sibling('td').text.strip().replace("-", "0")
                        dados = {
                            "Ano": str(year),
                            "Grupo": current_group,
                            "Produto": product,
                            "QuantidadeL": volume
                        }
                        all_data.append(dados)

        # Converter a lista de dicionários em JSON e escrever no arquivo específico
        file_path = json_files_dir + file_name
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(all_data, json_file, ensure_ascii=False, indent=4)

        print(f"{file_name} file was created successfully!")
    
    elif opt == 'opt_03' and subopt in ('subopt_01', 'subopt_02', 'subopt_03'):

        opt_subopt_files = {
            (opt, subopt): file_name,
        }
        
        for (opt, subopt), files in opt_subopt_files.items():
            all_data = [] 

            for year in range(start_year, end_year):
                params = {
                    'ano': year,
                    'opcao': opt,
                    'subopcao': subopt
                }
                
                response = requests.get(base_url, params=params, timeout=10000)
                soup = BeautifulSoup(response.text, 'html.parser')

                table = soup.find('table', class_='tb_base tb_dados')

                if table:
                    current_group = ""
                    for lines in table.find_all('tr'):
                        item = lines.find('td', class_='tb_item')
                        subitem = lines.find('td', class_='tb_subitem')
                        
                        if item:
                            current_group = item.text.strip() 
                            
                        if subitem and current_group:
                            cultivate = subitem.text.strip()
                            qty_kg = subitem.find_next_sibling('td').text.strip().replace("-", "0")
                            dados = {
                                "Ano": str(year),
                                "Grupo": current_group,
                                "Cultivar": cultivate,
                                "QuantidadeKg": qty_kg
                            }
                            all_data.append(dados)

            file_path = json_files_dir + files
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(all_data, json_file, ensure_ascii=False, indent=4)

            print(f"{files} file was created successfully!")

    elif opt == 'opt_03' and subopt == 'subopt_04':

        all_data = []  

        for year in range(start_year, end_year):  
            params = {
                'ano': year,
                'opcao': opt,
                'subopcao': subopt
            }
            
            response = requests.get(base_url, params=params, timeout=10000)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            table = soup.find('table', class_='tb_base tb_dados')

            if table:
                lines = table.find_all('tr')

                for lines in lines[1:-1]:  
                    coluns = lines.find_all('td')
                    if coluns and len(coluns) >= 2:
                        sem_definicao = coluns[0].text.strip()
                        qty_kg = coluns[1].text.strip().replace("-", "0")
                        dados = {
                            "Ano": str(year),
                            "SemDefinicao": sem_definicao,
                            "QuantidadeKg": qty_kg
                        }
                        all_data.append(dados)


        file_path = json_files_dir + file_name
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(all_data, json_file, ensure_ascii=False, indent=4)

        print(f"{file_name} file was created successfully!")

    else:
        print(f'The combination of parameters "{opt}" and "{subopt}" does not exist')

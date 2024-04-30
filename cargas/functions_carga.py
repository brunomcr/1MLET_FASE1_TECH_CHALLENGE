import requests
from bs4 import BeautifulSoup
import json
import os

# A base da URL
base_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php'

# Caminho para a pasta onde os arquivos JSON serão salvos
json_files_dir = 'json_files/'
if not os.path.exists(json_files_dir):
    os.mkdir(json_files_dir)


def get_data(opt, subopt, file_name, data_inicio, data_fim):
    if opt == 'opt_05' and subopt in ('subopt_01', 'subopt_02', 'subopt_03', 'subopt_04', 'subopt_05') \
    or opt == 'opt_06' and subopt in ('subopt_01', 'subopt_02', 'subopt_03', 'subopt_04'): 
        # Dicionário de opções e subopções com os nomes dos arquivos correspondentes
        opcoes_subopcoes_arquivos = {
        (opt, subopt): file_name,
        }

        # Itera pelas combinações de opções e subopções
        for (opcao, subopcao), arquivo in opcoes_subopcoes_arquivos.items():
            todos_dados = []  # Inicializa a lista de dados para cada combinação

            for ano in range(data_inicio, data_fim):
                # Os parâmetros da URL.
                params = {
                    'ano': ano,
                    'opcao': opcao,
                    'subopcao': subopcao
                }
                
                # Faz a requisição para o site com os parâmetros do ano específico.
                response = requests.get(base_url, params=params)
                soup = BeautifulSoup(response.text, 'html.parser')

                # Procura pela tabela com a classe específica.
                tabela = soup.find('table', class_='tb_base tb_dados')

                # Verifica se a tabela foi encontrada antes de continuar.
                if tabela:
                    # A lista de linhas da tabela
                    linhas = tabela.find_all('tr')[1:]  # Pula o cabeçalho.
                    
                    # Itera pelas linhas da tabela, excluindo a última linha que contém o total.
                    for linha in linhas[:-1]:
                        colunas = linha.find_all('td')
                        linha_dados = {
                            "Ano": str(ano),
                            "Pais": colunas[0].text.strip(),
                            "Quantidade": colunas[1].text.strip().replace("-", "0"),
                            "Valor": colunas[2].text.strip().replace("-", "0")
                        }
                        if linha_dados["Pais"]:  # Certifica-se de que a linha contém o nome do país.
                            todos_dados.append(linha_dados)
            
            # Converter a lista de dicionários em JSON e escrever no arquivo específico
            with open(json_files_dir + arquivo, 'w', encoding='utf-8') as json_file:
                json.dump(todos_dados, json_file, ensure_ascii=False, indent=4)

            print(f"Arquivo {arquivo} criado com sucesso.")
    
    elif opt == 'opt_02' and subopt == None \
    or opt == 'opt_04' and subopt == None:
        # Inicializa a lista de dados
        todos_dados = []  

        for ano in range(data_inicio, data_fim):
            # Os parâmetros da URL
            params = {
                'ano': ano,
                'opcao': opt,
                'subopcao': subopt
            }
            
            # Faz a requisição para o site com os parâmetros do ano específico
            response = requests.get(base_url, params=params)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Procura pela tabela com a classe específica
            tabela = soup.find('table', class_='tb_base tb_dados')

            # Verifica se a tabela foi encontrada antes de continuar
            if tabela:
                grupo_atual = ""  # Inicializa o grupo atual

                # Itera pelas linhas da tabela
                for linha in tabela.find_all('tr'):
                    item = linha.find('td', class_='tb_item')
                    subitem = linha.find('td', class_='tb_subitem')

                    if item:
                        grupo_atual = item.text.strip()  # Atualiza o grupo atual quando um novo tb_item é encontrado
                    
                    if subitem and grupo_atual:  # Processa subitens se um grupo está definido
                        produto = subitem.text.strip()
                        quantidade_l = subitem.find_next_sibling('td').text.strip().replace("-", "0")
                        dados = {
                            "Ano": str(ano),
                            "Grupo": grupo_atual,
                            "Produto": produto,
                            "QuantidadeL": quantidade_l
                        }
                        todos_dados.append(dados)

        # Converter a lista de dicionários em JSON e escrever no arquivo específico
        arquivo_caminho = json_files_dir + file_name
        with open(arquivo_caminho, 'w', encoding='utf-8') as json_file:
            json.dump(todos_dados, json_file, ensure_ascii=False, indent=4)

        print(f"Arquivo {file_name} criado com sucesso.")
    
    elif opt == 'opt_03' and subopt in ('subopt_01', 'subopt_02', 'subopt_03'):
        # Dicionário de opções e subopções com os nomes dos arquivos correspondentes
        opcoes_subopcoes_arquivos = {
            (opt, subopt): file_name,
        }
        # Itera pelas combinações de opções e subopções
        for (opcao, subopcao), arquivo in opcoes_subopcoes_arquivos.items():
            todos_dados = []  # Inicializa a lista de dados para cada combinação

            for ano in range(data_inicio, data_fim):
                # Os parâmetros da URL.
                params = {
                    'ano': ano,
                    'opcao': opcao,
                    'subopcao': subopcao
                }
                
                # Faz a requisição para o site com os parâmetros do ano específico.
                response = requests.get(base_url, params=params)
                soup = BeautifulSoup(response.text, 'html.parser')

                # Procura pela tabela com a classe específica.
                tabela = soup.find('table', class_='tb_base tb_dados')

                # Verifica se a tabela foi encontrada antes de continuar.
                if tabela:
                    grupo_atual = ""
                    # Itera pelas linhas da tabela.
                    for linha in tabela.find_all('tr'):
                        item = linha.find('td', class_='tb_item')
                        subitem = linha.find('td', class_='tb_subitem')
                        
                        if item:
                            grupo_atual = item.text.strip()  # Define o grupo atual
                            
                        if subitem and grupo_atual:  # Se 'tb_subitem' e temos um grupo atual definido
                            cultivar = subitem.text.strip()
                            # A próxima 'td' deve conter a quantidade
                            quantidade_kg = subitem.find_next_sibling('td').text.strip().replace("-", "0")
                            dados = {
                                "Ano": str(ano),
                                "Grupo": grupo_atual,
                                "Cultivar": cultivar,
                                "QuantidadeKg": quantidade_kg
                            }
                            todos_dados.append(dados)

            # Converter a lista de dicionários em JSON e escrever no arquivo específico
            arquivo_caminho = json_files_dir + arquivo
            with open(arquivo_caminho, 'w', encoding='utf-8') as json_file:
                json.dump(todos_dados, json_file, ensure_ascii=False, indent=4)

            print(f"Arquivo {arquivo} criado com sucesso.")

    elif opt == 'opt_03' and subopt == 'subopt_04':
        # Define o arquivo para os dados de uvas sem classificação
        todos_dados = []  # Inicializa a lista de dados

        for ano in range(data_inicio, data_fim):  # Ajuste a faixa de anos conforme necessário
            # Os parâmetros da URL
            params = {
                'ano': ano,
                'opcao': opt,
                'subopcao': subopt
            }
            
            # Faz a requisição para o site com os parâmetros do ano específico
            response = requests.get(base_url, params=params)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Procura pela tabela com a classe específica
            tabela = soup.find('table', class_='tb_base tb_dados')

            # Verifica se a tabela foi encontrada antes de continuar
            if tabela:
                linhas = tabela.find_all('tr')
                # Itera pelas linhas da tabela, excluindo o cabeçalho e o rodapé (total)
                for linha in linhas[1:-1]:  # Pula a primeira linha (cabeçalho) e ignora a última linha (total)
                    colunas = linha.find_all('td')
                    if colunas and len(colunas) >= 2:
                        sem_definicao = colunas[0].text.strip()
                        quantidade_kg = colunas[1].text.strip().replace("-", "0")
                        dados = {
                            "Ano": str(ano),
                            "SemDefinicao": sem_definicao,
                            "QuantidadeKg": quantidade_kg
                        }
                        todos_dados.append(dados)

        # Converter a lista de dicionários em JSON e escrever no arquivo específico
        arquivo_caminho = json_files_dir + file_name
        with open(arquivo_caminho, 'w', encoding='utf-8') as json_file:
            json.dump(todos_dados, json_file, ensure_ascii=False, indent=4)

        print(f"Arquivo {file_name} criado com sucesso.")
   
    else:
        print(f'A combinação entre a opção "{opt}" e subopcao "{subopt}" não existe')



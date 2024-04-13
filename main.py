import os
import requests
import re


# Limpa o terminal
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Obter os nomes dos arquivos CSV
url = "http://vitibrasil.cnpuv.embrapa.br/download/"
response = requests.get(url)
html = response.content.decode()

# Extrair os nomes dos arquivos CSV
arquivos = []
for match in re.findall(r'href="(.*?.csv)', html):
    arquivos.append(match)

# Diretorio para arquivos CSV, se nao existir cria um.
arquivos_csv = 'arquivos_csv/'
if not os.path.exists(arquivos_csv):
    os.mkdir(arquivos_csv)

# Baixar os arquivos CSV
print('\n*** INICIANDO DOWNLOAD DOS ARQUIVOS ***\n')
print('ARQUIVOS: \n')

for item in arquivos:
    file_url = url + item
    response = requests.get(file_url)
    with open(arquivos_csv+item, "wb") as f:
        f.write(response.content)

    print(f'{item} baixado!')

# Listando os arquivos criado
total_arquivos = len(os.listdir(arquivos_csv))
print (f'Todos os {total_arquivos} arquivos foram baixados! 👍 \n')

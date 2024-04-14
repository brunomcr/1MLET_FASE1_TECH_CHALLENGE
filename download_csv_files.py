import os
import requests
import re

# Clear the terminal / Limpa o terminal
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Fetch CSV file names / Obter os nomes dos arquivos CSV
url = "http://vitibrasil.cnpuv.embrapa.br/download/"
response = requests.get(url)
html = response.content.decode()

# Extract CSV file names / Extrair os nomes dos arquivos CSV
csv_files = []
for match in re.findall(r'href="(.*?.csv)', html):
    csv_files.append(match)

# Directory for CSV files, create if it does not exist. / Diretório para arquivos CSV, se não existir, cria um.
csv_files_dir = 'csv_files/'
if not os.path.exists(csv_files_dir):
    os.mkdir(csv_files_dir)

# Download CSV files / Baixar os arquivos CSV
print('\n*** STARTING DOWNLOAD OF FILES ***\n')
print('FILES: \n')

for item in csv_files:
    file_url = url + item
    response = requests.get(file_url)
    with open(csv_files_dir + item, "wb") as f:
        f.write(response.content)

    print(f'{item} downloaded!')

# List created files / Listando os arquivos criados
total_files = len(os.listdir(csv_files_dir))
print(f'All {total_files} files have been downloaded! 👍 \n')

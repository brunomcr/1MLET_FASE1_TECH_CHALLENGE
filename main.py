import os
import requests
import re

os.system('clear') # Se estiver utilizando Windows👀 altere DE: 'clear' PARA: 'cls'

# Obter os nomes dos arquivos CSV
url = "http://vitibrasil.cnpuv.embrapa.br/download/"
response = requests.get(url)
html = response.content.decode()

# Extrair os nomes dos arquivos CSV
arquivos = []
for match in re.findall(r'href="(.*?.csv)', html):
    arquivos.append(match)

# Baixar os arquivos CSV
arquivos_csv = 'arquivos_csv/'
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

import pandas as pd
from db_connection import connect_to_docker_db
import os

# Connect to MongoDB / Conexão ao MongoDB
db = connect_to_docker_db('1mlet_embrapa2')

# Directory that contains the CSV files / Diretório que contém os arquivos CSV
csv_directory = 'csv_files'

# List of CSV files / Lista de arquivos CSV
csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]

# Load each CSV file into a MongoDB collection
# Carregar cada arquivo CSV para uma coleção no MongoDB
for file in csv_files:
    collection_name = file.split('.')[0]  # Collection name based on the file name
    df = pd.read_csv(os.path.join(csv_directory, file), sep=';')
    db[collection_name].insert_many(df.to_dict('records'))

print("Data loaded successfully!")

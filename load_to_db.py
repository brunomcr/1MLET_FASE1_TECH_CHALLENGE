import pandas as pd
from db_connection import connect_to_local_db, connect_to_docker_db
import os
import json  # Import necessário para lidar com arquivos JSON


# Connect to MongoDB / Conexão ao MongoDB
db = connect_to_local_db('1mlet_embrapa')

# Directory that contains the JSON files / Diretório que contém os arquivos JSON
json_directory = 'cargas/json_files'

# List of JSON files / Lista de arquivos JSON
json_files = [f for f in os.listdir(json_directory) if f.endswith('.json')]

# Load each JSON file into a MongoDB collection
for file in json_files:
    collection_name = file.split('.')[0]  # Collection name based on the file name
    # Load JSON file specifying the encoding
    with open(os.path.join(json_directory, file), 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    db[collection_name].insert_many(data)

print("Data loaded successfully!")

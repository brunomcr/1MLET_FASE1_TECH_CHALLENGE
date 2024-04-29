from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pymongo.errors import ServerSelectionTimeoutError


def connect_to_local_db(db_name):
    """
    Connects to DB and return a database object
    :param db_name: str, name of the db
    :return: db object
    """
    client = MongoClient('mongodb://localhost:27017/')  # ⚠️ Need to change "localhost" to service name in Docker
    db = client[db_name]
    return db


def connect_to_docker_db(db_name):

    # Carrega .env
    load_dotenv()

    # Pega variaveis de ambient (.env)
    mongo_user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    mongo_pass = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
    print(f"Mongo User: {mongo_user}")
    print(f"Mongo Pass: {mongo_pass}")

    # Gera uri para conexao
    uri = f"mongodb://{mongo_user}:{mongo_pass}@mongo-db:27017/"
    print(f"uri: {uri}")

    # tenta conecatar no banco
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=10000)
        # Verifica informacoes da conexao
        client.server_info()
    except ServerSelectionTimeoutError as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None

    # Seleciona o banco de dados.
    db = client[db_name]
    print(f"db: {db}")

    return db



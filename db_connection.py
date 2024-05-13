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
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    return db


def connect_to_docker_db(db_name):
    load_dotenv()

    mongo_user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    mongo_pass = os.getenv('MONGO_INITDB_ROOT_PASSWORD')

    try:
        client = MongoClient(host='localhost', #mongo-db
                             port=27017,
                             username=mongo_user,
                             password=mongo_pass,
                             authSource='admin')
        client.server_info()  # Testa a conexão
    except ServerSelectionTimeoutError as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None

    db = client[db_name]
    return db




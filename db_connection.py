from pymongo import MongoClient


def connect_to_db(db_name):
    """
    Connects to DB and return a database object
    :param db_name: str, name of the db
    :return: db object
    """
    client = MongoClient('mongodb://localhost:27017/')  # ⚠️ Need to change "localhost" to service name in Docker
    db = client[db_name]
    return db
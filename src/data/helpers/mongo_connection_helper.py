from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pymongo.errors import ServerSelectionTimeoutError
from ..interfaces import ConnectionHelper

class MongoConnectionHelper(ConnectionHelper):
    def connect(self, db_name):
        load_dotenv()

        mongo_user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
        mongo_pass = os.getenv('MONGO_INITDB_ROOT_PASSWORD')

        try:
            client = MongoClient(host='localhost', 
                                port=27017,
                                username=mongo_user,
                                password=mongo_pass,
                                authSource='admin')
            client.server_info() 
        except ServerSelectionTimeoutError as e:
            print(f"Error connecting to MongoDB: {e}")
            return None
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return None

        db = client[db_name]
        return db

from ..services.interfaces.repositories import ProductionRepository
from .repositories import ProductionRepositoryImpl
from .helpers import MongoConnectionHelper
from .interfaces import ConnectionHelper


production_repository = ProductionRepositoryImpl()
connection_helper = MongoConnectionHelper().connect('1mlet_embrapa')


def get_production_repository() -> ProductionRepository:
    return production_repository

def get_database_connection() -> ConnectionHelper:
    return connection_helper
    

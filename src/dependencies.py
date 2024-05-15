from src.domain.interfaces import ProductionService, DBPopulatorService
from src.services import ProductionServiceImpl, DBPopulatorServiceImpl
from src.services.interfaces.repositories import ProductionRepository
from src.data.repositories import ProductionRepositoryImpl
from src.data.helpers import MongoConnectionHelper
from src.data.interfaces import ConnectionHelper


production_service = ProductionServiceImpl()
production_repository = ProductionRepositoryImpl()
connection_helper = MongoConnectionHelper().connect('1mlet_embrapa')
db_populator_service = DBPopulatorServiceImpl()


def get_production_service() -> ProductionService:
    return production_service

def get_production_repository() -> ProductionRepository:
    return production_repository()

def get_database_connection() -> ConnectionHelper:
    return connection_helper()

def get_db_populator_service() -> DBPopulatorService:
    return db_populator_service

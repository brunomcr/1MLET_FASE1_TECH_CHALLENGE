from ..domain.interfaces import ProductionService, DBPopulatorService
from . import ProductionServiceImpl, DBPopulatorServiceImpl


production_service = ProductionServiceImpl()
db_populator_service = DBPopulatorServiceImpl()


def get_production_service() -> ProductionService:
    return production_service

def get_db_populator_service() -> DBPopulatorService:
    return db_populator_service

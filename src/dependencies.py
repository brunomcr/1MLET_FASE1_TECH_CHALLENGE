from domain import *
from data import *
from services import *


def get_production_service() -> ProductionService:
    return ProductionServiceImpl()


def get_production_repository() -> ProductionRepository:
    return ProductionRepositoryImpl()

from src.di import Injector
from src.domain import ProductionService
from src.services import ProductionServiceImpl


injector = Injector()
injector.register(ProductionService, ProductionServiceImpl())

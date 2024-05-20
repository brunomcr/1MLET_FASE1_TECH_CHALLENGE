from src.di import Injector
from src.domain import ProductionDataService
from src.services import ProductionDataDataServiceImpl


injector = Injector()
injector.register(ProductionDataService, ProductionDataDataServiceImpl())

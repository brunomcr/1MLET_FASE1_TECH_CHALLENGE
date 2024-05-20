from src.di import Injector
from src.domain import ProcessingDataService, ProductionDataService
from src.services import ProcessingDataServiceImpl, ProductionDataServiceImpl


injector = Injector()
injector.register(ProcessingDataService, ProcessingDataServiceImpl())
injector.register(ProductionDataService, ProductionDataServiceImpl())

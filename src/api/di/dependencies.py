from src.di import Injector
from src.domain import ProcessingDataService, ProductionDataService, ImportDataService
from src.services import ProcessingDataServiceImpl, ProductionDataServiceImpl, ImportDataServiceImpl


injector = Injector()
injector.register(ProcessingDataService, ProcessingDataServiceImpl())
injector.register(ProductionDataService, ProductionDataServiceImpl())
injector.register(ImportDataService, ImportDataServiceImpl())



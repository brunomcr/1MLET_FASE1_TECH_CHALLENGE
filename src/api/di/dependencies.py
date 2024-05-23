from ...di import Injector
from ...domain.interfaces.services import *
from ...services import *

injector = Injector()
injector.register(ImportDataService, ImportDataServiceImpl())
injector.register(JWTTokenService, JWTTokenServiceImpl())
injector.register(ProcessingDataService, ProcessingDataServiceImpl())
injector.register(ProductionDataService, ProductionDataServiceImpl())
injector.register(TradingDataService, TradingDataServiceImpl())

from .di import Injector
from .domain.interfaces.services import DBPopulatorService
from .services import DBPopulatorServiceImpl


injector = Injector()
injector.register(DBPopulatorService, DBPopulatorServiceImpl())

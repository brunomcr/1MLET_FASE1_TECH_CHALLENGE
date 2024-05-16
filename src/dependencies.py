from src.di import Injector
from src.domain import DBPopulatorService
from src.services import DBPopulatorServiceImpl


injector = Injector()
injector.register(DBPopulatorService, DBPopulatorServiceImpl())

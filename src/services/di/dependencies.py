from ...data.helpers import MongoDatabaseHelper
from ...data.interfaces import DatabaseHelper
from ...data.repositories import *
from ...di import Injector
from ..interfaces import *


injector = Injector()

injector.register(DatabaseHelper, MongoDatabaseHelper())
injector.register(ExportDataRepository, ExportDataRepositoryImpl())
injector.register(ImportDataRepository, ImportDataRepositoryImpl())
injector.register(ProcessingDataRepository, ProcessingDataRepositoryImpl())
injector.register(ProductionDataRepository, ProductionDataRepositoryImpl())
injector.register(TradingnDataRepository, TradingDataRepositoryImpl())

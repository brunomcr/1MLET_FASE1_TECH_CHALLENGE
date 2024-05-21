from src.data.helpers import MongoDatabaseHelper
from src.data.interfaces import DatabaseHelper
from src.data.repositories import ProductionDataRepositoryImpl, ProcessingDataRepositoryImpl, ImportDataRepositoryImpl
from src.di import Injector
from ..interfaces import ProcessingDataRepository, ProductionDataRepository, ImportDataRepository

injector = Injector()

injector.register(DatabaseHelper, MongoDatabaseHelper())
injector.register(ProcessingDataRepository, ProcessingDataRepositoryImpl())
injector.register(ProductionDataRepository, ProductionDataRepositoryImpl())
injector.register(ImportDataRepository, ImportDataRepositoryImpl())

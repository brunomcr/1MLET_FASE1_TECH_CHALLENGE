from src.data.helpers import MongoDatabaseHelper
from src.data.interfaces import DatabaseHelper
from src.data.repositories import ProductionDataRepositoryImpl, ProcessingDataRepositoryImpl
from src.di import Injector
from ..interfaces import ProcessingDataRepository, ProductionDataRepository

injector = Injector()

injector.register(DatabaseHelper, MongoDatabaseHelper())
injector.register(ProcessingDataRepository, ProcessingDataRepositoryImpl())
injector.register(ProductionDataRepository, ProductionDataRepositoryImpl())

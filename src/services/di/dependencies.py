from src.data.helpers import MongoDatabaseHelper
from src.data.interfaces import DatabaseHelper
from src.data.repositories import ProductionDataRepositoryImpl
from src.di import Injector
from src.services.interfaces import ProductionDataRepository

injector = Injector()

injector.register(DatabaseHelper, MongoDatabaseHelper())
injector.register(ProductionDataRepository, ProductionDataRepositoryImpl())

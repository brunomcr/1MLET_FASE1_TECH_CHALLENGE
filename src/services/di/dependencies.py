from src.data.helpers import MongoDatabaseHelper
from src.data.interfaces import DatabaseHelper
from src.data.repositories import ProductionRepositoryImpl
from src.di import Injector
from src.services.interfaces import ProductionRepository

injector = Injector()

injector.register(DatabaseHelper, MongoDatabaseHelper())
injector.register(ProductionRepository, ProductionRepositoryImpl())

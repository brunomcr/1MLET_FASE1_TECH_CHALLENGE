from src.data import ProductionRepositoryImpl
from src.data.helpers import MongoDatabaseHelper
from src.data.interfaces import DatabaseHelper
from src.di import Injector
from src.services import ProductionRepository

injector = Injector()

injector.register(DatabaseHelper, MongoDatabaseHelper())
injector.register(ProductionRepository, ProductionRepositoryImpl())

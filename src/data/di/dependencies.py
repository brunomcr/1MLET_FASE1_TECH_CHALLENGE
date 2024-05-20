from src.data.helpers import MongoDatabaseHelper
from src.data.interfaces import DatabaseHelper
from src.di import Injector

injector = Injector()

injector.register(DatabaseHelper, MongoDatabaseHelper())

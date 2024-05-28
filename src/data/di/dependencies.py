from ...data.helpers import MongoDatabaseHelper
from ...data.interfaces import DatabaseHelper
from ...di import Injector

injector = Injector()

injector.register(DatabaseHelper, MongoDatabaseHelper())

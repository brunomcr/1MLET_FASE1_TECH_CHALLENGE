from abc import ABC, abstractmethod


class DatabaseHelper(ABC):
    @abstractmethod
    def connect(self, db_name):
        raise NotImplementedError

    @abstractmethod
    def insert_many(self, collection, data):
        raise NotImplementedError

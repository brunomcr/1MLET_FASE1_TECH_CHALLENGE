from abc import ABC, abstractmethod


class DBPopulatorService(ABC):
    @abstractmethod
    def populate(self):
        raise NotImplementedError

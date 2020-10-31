import abc
from domain.serializable import Serializable


class Desk(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def get(page) -> list:
        pass

    @staticmethod
    @abc.abstractmethod
    def add(entry):
        pass

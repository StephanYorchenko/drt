import abc
import typing


class Serializable(abc.ABC):
    def to_json(self) -> typing.Dict[str, str]:
        res = {}
        for name, value in self.__dict__.items():
            if not name.startswith('_'):
                res[name] = value
        return res

    @staticmethod
    @abc.abstractmethod
    def from_json(data: typing.Dict[str, str]):
        pass

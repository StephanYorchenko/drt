import abc
import typing


class Serializable(abc.ABC):
    def to_json(self) -> typing.Dict[str]:
        res = {}
        for name, value in self.__dict__.items():
            if name[0] != '_':
                res[name] = value
        return res

    @staticmethod
    @abc.abstractmethod
    def from_json(data: typing.Dict[str]):
        pass

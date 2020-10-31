import abc


class Serializable(abc.ABC):
    def to_json(self) -> bytes:
        pass

    @staticmethod
    def from_json(data: bytes):
        pass

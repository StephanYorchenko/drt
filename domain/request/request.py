import typing

from .requestType import HostessRequestType
from infrastructure.serializable import Serializable


class Request(Serializable):
    def __init__(self,
                 request_id: int,
                 request_type: HostessRequestType,
                 comment: str,
                 user_id: int):
        self._type = request_type
        self._comment = comment
        self._id = request_id
        self._user = user_id

    @property
    def request_id(self) -> int:
        return self._id

    @property
    def comment(self) -> str:
        return self._comment

    @property
    def request_type(self) -> HostessRequestType:
        return self._type

    @property
    def user_id(self) -> int:
        return self._user

    def __eq__(self, other):
        if other is not Request:
            return False

        return self.request_id == other.id

    def to_json(self) -> typing.Dict[str]:
        return {'id': self._id, 'request_type': self._type,
                'comment': self._comment, 'user_id': self._user}

    @staticmethod
    def from_json(data: typing.Dict[str]):
        return Request(data['id'], data['request_type'], data['comment'],
                       data['user_id'])

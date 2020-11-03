from __future__ import annotations
from typing import Dict

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

    def to_json(self) -> Dict[str, str]:
        return {'id': self._id, 'request_type': self._type,
                'comment': self._comment, 'user_id': self._user}

    @staticmethod
    def from_json(data: Dict[str, str]) -> Request:
        return Request(int(data['id']),
                       HostessRequestType(data['request_type']),
                       data['comment'],
                       int(data['user_id']))

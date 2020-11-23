from __future__ import annotations

from .requestType import HostessRequestType


class Request:
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
import typing
from .HostessRequestType import HostessRequestType


class Request:
    def __init__(self,
                 request_type: HostessRequestType,
                 comment: str,
                 request_id: int):
        self._type = request_type
        self._comment = comment
        self._id = request_id

    @property
    def request_id(self):
        return self._id

    @property
    def comment(self):
        return self._comment

    @property
    def request_type(self):
        return self._type

from dataclasses import dataclass

from .requestType import HostessRequestType


@dataclass
class Request:
    request_id: int
    request_type: HostessRequestType
    comment: str
    user_id: int
    date: str
    is_watched: bool

    def __eq__(self, other):
        if other is not Request:
            return False
        return self.request_id == other.request_id

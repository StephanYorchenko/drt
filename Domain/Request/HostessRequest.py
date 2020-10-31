from .HostessRequestType import HostessRequestType
from Domain.Users.User import User


class HostessRequest:
    def __init__(self,
                 request_id: int,
                 request_type: HostessRequestType,
                 comment: str,
                 user: User):
        self._type = request_type
        self._comment = comment
        self._id = request_id
        self._user = user

    @property
    def request_id(self) -> int:
        return self._id

    @property
    def comment(self) -> str:
        return self._comment

    @property
    def request_type(self) -> HostessRequestType:
        return self._type

    def __eq__(self, other):
        if other is not HostessRequest:
            return False

        return self.request_id == other.id

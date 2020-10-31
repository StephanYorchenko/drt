import typing

from .User import User
from .Roles import Role
from Domain.Request import HostessRequest


class Hostess(User):
    def __init__(self, user_id: int, username: str, password):
        super().__init__(user_id, username, password, Role.HOSTESS)

    def get_requests(self) -> typing.List[HostessRequest]:
        pass

    def accept_request(self, request):
        pass

    def deny_request(self, request):
        pass

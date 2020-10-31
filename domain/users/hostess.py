import typing

from .user import User
from .roles import Role
from domain.request.request import Request


class Hostess(User):
    def __init__(self, user_id: int, username: str, password):
        super().__init__(user_id, username, password, Role.HOSTESS)

    def get_requests(self) -> typing.List[Request]:
        pass

    def accept_request(self, request: Request) -> None:
        pass

    def deny_request(self, request: Request) -> None:
        pass

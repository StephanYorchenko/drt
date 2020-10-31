import typing
from .Roles import Role
from .HostessRequest import Request
from .Table import Table


class User:
    def __init__(self, user_id: int, role: Role):
        self.id = user_id
        self.role = role

    def make_request(self, topic: str, description: str):
        pass

    def try_book_table(self, table: Table):
        pass

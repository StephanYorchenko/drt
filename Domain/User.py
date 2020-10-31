import typing
from .Roles import Role
from .HostessRequest import HostessRequest
from .Table import Table


class User:
    def __init__(self, user_id: int, role: Role, login: str, password: str):
        self.id = user_id
        self.role = role
        self.login = login
        self.set_password(password)

    def set_password(self, password: str):
        pass

    def make_request(self, topic: str, description: str):
        pass

    def try_book_table(self, table: Table):
        pass

import typing
import json
from .Roles import Role
from .HostessRequest import HostessRequest
from .Table import Table


class User:
    def __init__(self, user_id: int, role: Role, username: str, password):
        self.id = user_id
        self.role = role
        self.username = username
        self.password = password

    def set_username(self, username: str) -> None:
        self.username = username

    def set_password(self, password) -> None:
        self.password = password

    def make_request(self, topic: str, description: str):
        pass

    def try_book_table(self, table: Table) -> bool:
        pass

    def to_json(self) -> bytes:
        return bytes(json.dumps({'id': self.id,
                                 'role': self.role,
                                 'username': self.username,
                                 'password': self.password}))

    @staticmethod
    def from_json(data: bytes):
        dictionary = json.loads(data)
        return User(dictionary['id'],
                    dictionary['role'],
                    dictionary['username'],
                    dictionary['password'])

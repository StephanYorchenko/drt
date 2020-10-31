import typing
import json
from .Roles import Role
from .HostessRequest import HostessRequest
from .Serializable import Serializable
from .Table import Table
from abc import ABC


class User(ABC, Serializable):
    def __init__(self, user_id: int, username: str, password):
        self.id = user_id
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

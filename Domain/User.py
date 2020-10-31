from abc import ABC

from .Serializable import Serializable
from .Table import Table


class User(ABC, Serializable):
    def __init__(self, user_id: int, username: str, password):
        self.id = user_id
        self.username = username
        self.password = password
        self.role = None

    def set_username(self, username: str) -> None:
        self.username = username

    def set_password(self, password) -> None:
        self.password = password

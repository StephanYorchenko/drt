from abc import ABC

from Domain.Serializable import Serializable
from .Roles import Role


class User(ABC, Serializable):
    def __init__(self, user_id: int, username: str, password, role: Role):
        self.id = user_id
        self.username = username
        self.password = password
        self.role = role

    def set_username(self, username: str) -> None:
        self.username = username

    def set_password(self, password) -> None:
        self.password = password

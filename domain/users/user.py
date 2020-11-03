from abc import ABC

from infrastructure.serializable import Serializable
from .roles import Role


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

    @staticmethod
    def from_json(data):
        return User(data['id'], data['username'], data['password'],
                    data['role'])

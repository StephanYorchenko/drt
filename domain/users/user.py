from __future__ import annotations
from abc import ABC
from dataclasses import dataclass

from .roles import Role


@dataclass
class User(ABC):
    user_id: int
    username: str
    password: str
    role: Role

    def set_username(self, username: str) -> None:
        self.username = username

    def set_password(self, password) -> None:
        self.password = password

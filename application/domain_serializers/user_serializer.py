from typing import Dict
from .domain_serializer import DomainSerializer
from domain.users.user import User
from domain.users.roles import Role


def from_json(data: Dict[str, str]) -> User:
    return User(int(data['id']), data['username'], data['password'],
                Role(data['role']))


class UserSerializer(DomainSerializer):
    def __init__(self):
        super().__init__(from_json)

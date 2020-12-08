from typing import Dict
from .domain_transformer import DomainTransformer
from domain.users.user import User
from domain.users.roles import Role


def from_json(data: Dict[str, str]) -> User:
    return User(int(data['id']), data['username'], data['password'],
                Role(data['role']))


class UserTransformer(DomainTransformer):
    def __init__(self):
        super().__init__(lambda record: User(record.id, record.username,
                         record.password, Role(record.role)))

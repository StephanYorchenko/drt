from typing import Dict
from .domain_serializer import DomainSerializer
from domain.users.user import User
from domain.users.roles import Role


class UserSerializer(DomainSerializer):
    def from_json(self, data: Dict[str, str]) -> User:
        return User(int(data['id']), data['username'], data['password'],
                    Role(data['role']))

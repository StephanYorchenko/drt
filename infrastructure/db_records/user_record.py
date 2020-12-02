from dataclasses import dataclass
from infrastructure.db_classes.db_user import DBUser


@dataclass
class UserRecord:
    id: int
    name: str
    password: str
    user_hash: str
    role: str

    @staticmethod
    def from_db_type(request: DBUser):
        return Request(
            request.id,
            request.name,
            request.password,
            request.user_hash,
            request.role
        )

from dataclasses import dataclass
from infrastructure import db_classes


@dataclass
class UserRecord:
    id: int
    name: str
    password: str
    user_hash: str
    role: str

    @staticmethod
    def from_db_type(request: db_classes.db_user.DBUser):
        return Request(
            request.id,
            request.name,
            request.password,
            request.user_hash,
            request.role
        )

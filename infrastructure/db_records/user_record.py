from dataclasses import dataclass


@dataclass
class UserRecord:
    id: int
    name: str
    password: str
    user_hash: str
    role: str

    @staticmethod
    def from_db_type(request):
        return UserRecord(
            request.id,
            request.name,
            request.password,
            request.user_hash,
            request.role
        )

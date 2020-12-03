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
        if request is None:
            return None
        return UserRecord(
            request.id,
            request.name,
            request.password,
            request.user_hash,
            request.role
        )

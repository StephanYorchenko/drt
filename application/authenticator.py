from typing import Optional
from infrastructure import DBUser
from infrastructure.db_records.user_record import UserRecord


class Authenticator:
    def __init__(self, db_user: DBUser):
        self.db_user = db_user

    def check_auth(self, user: str, user_hash: str) -> bool:
        result = self.db_user.check_user(user, user_hash)
        return result

    def get_user(self, username: str) -> Optional[UserRecord]:
        return self.db_user.get_user(name=username)

    def get_authenticated_user(self, username: str, password: str):
        user = self.get_user(username)
        if user is None or user.password != password:
            return None

        return user

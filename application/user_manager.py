from typing import Optional
from infrastructure import DBUser
from infrastructure.db_records.user_record import UserRecord


class UserManager:
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

    def add_user(self, username: str, password: str, role: str):
        user = self.db_user.get_user(name=username)
        if user is not None:
            return False
        try:
            self.db_user.add_user(name=username, password=password, role=role)
        except ValueError:
            return False

        return True

    def update_user(
            self,
            current_name,
            new_name=None,
            new_password=None,
            new_role=None
    ):
        user = self.get_user(current_name)
        if user is None:
            return False

        if new_name is not None:
            self.db_user.update_username(user.id, new_name)
        if new_password is not None:
            self.db_user.update_password(user.id, new_password)
        if new_role is not None:
            try:
                self.db_user.update_role(user.id, new_role)
            except ValueError:
                return False

        return True

    def get_all_users(self):
        return self.db_user.get_all()

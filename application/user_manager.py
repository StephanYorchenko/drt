from typing import Optional, List
import sys

from application.transformers.user_record_transformer \
    import UserRecordTransformer
from domain import Role, User
from infrastructure import DBUser


class UserManager:
    def __init__(self, db_user: DBUser, transformer: UserRecordTransformer):
        self.db_user = db_user
        self.transformer = transformer

    def get_role(self, username: str) -> Role:
        return self.get_user(username).role

    def check_rights(self, name, *roles):
        if self.get_role(name) not in roles:
            raise PermissionError

    def check_auth(self, user: str, user_hash: str) -> bool:
        result = self.db_user.check_user(user, user_hash)
        return result

    def get_user(self, username: str) -> Optional[User]:
        # noinspection PyUnresolvedReferences
        record = self.db_user.get_user(name=username)
        return self.transformer.from_record(record) \
            if record is not None \
            else None

    def get_authenticated_user(self, username: str,
                               password: str) -> Optional[User]:
        user = self.get_user(username)
        if user is None or user.password != password:
            return None

        return user

    def add_user(self, username: str, password: str, role: int,
                 caller_name: str):
        self.check_rights(caller_name, Role.ADMIN)
        user = self.db_user.get_user(name=username)
        try:
            Role(role)
        except ValueError as e:
            print(f"Couldn't add user {username}, {e}", file=sys.stderr)
            return
        if user is not None:
            return False
        try:
            self.db_user.add_user(name=username, password=password, role=role)
        except ValueError:
            return False

        return True

    def delete_user(self, name: str, caller_name: str):
        self.check_rights(caller_name, Role.ADMIN)
        result = self.db_user.delete_user(name=name)
        return True

    def update_user(
            self,
            current_name,
            caller_name: str,
            new_name: str = None,
            new_password: str = None,
            new_role: int = None
    ):
        self.check_rights(caller_name, Role.ADMIN)
        user = self.get_user(current_name)
        if user is None:
            return False

        if new_name is not None:
            self.db_user.update_username(user.user_id, new_name)
        if new_password is not None:
            self.db_user.update_password(user.user_id, new_password)
        if new_role is not None:
            try:
                Role(new_role)
            except ValueError as e:
                print(f"Couldn't update user {current_name}, {e}",
                      file=sys.stderr)
                return
            try:
                self.db_user.update_role(user.user_id, new_role)
            except ValueError:
                return False

        return True

    def update_user_hash(self, name, token):
        self.db_user.update_user_hash(name, token)

    def get_all_users(self, caller_name: str) -> List[User]:
        self.check_rights(caller_name, Role.ADMIN)
        return list(map(self.transformer.from_record, self.db_user.get_all()))

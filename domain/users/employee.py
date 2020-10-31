from domain.users.user import User
from domain.users.roles import Role
from infrastructure.DBRequests import DBRequest


class Employee(User):
    def __init__(self, user_id: int, username: str, password: str):
        super().__init__(user_id, username, password, Role.EMPLOYEE)

    def make_request(self, request: DBRequest):
        pass

    def try_book_table(self, table):
        pass

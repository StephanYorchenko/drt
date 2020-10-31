from domain.users import user
from domain.users.roles import Role
from infrastructure.DBRequests import Request


class Employee(user):
    def __init__(self, user_id: int, username: str, password: str):
        super().__init__(user_id, username, password, Role.EMPLOYEE)

    def make_request(self, request: Request):
        pass

    def try_book_table(self, table):
        pass

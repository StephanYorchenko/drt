from Domain.Users import User
from Domain.Users.Roles import Role
from Infrastructure.DBRequests import Request


class Employee(User):
    def __init__(self, user_id: int, username: str, password: str):
        super().__init__(user_id, username, password, Role.EMPLOYEE)

    def make_request(self, request: Request):
        pass

    def try_book_table(self, table):
        pass

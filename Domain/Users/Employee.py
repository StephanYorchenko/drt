from Domain.User import User
from Domain.Roles import Role
from Infrastructure.requests import Request


class Employee(User):
    def __init__(self, user_id: int, username: str, password: str):
        super().__init__(user_id, username, password, Role.EMPLOYEE)

    def make_request(self, request: Request):
        pass

    def try_book_table(self, table):
        pass

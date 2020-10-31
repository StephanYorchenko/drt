from Domain.User import User
from Domain.Roles import Role


class Employee(User):
    def __init__(self, user_id: int, username: str, password: str):
        super().__init__(user_id, username, password, Role.EMPLOYEE)

    def
from .employee import Employee
from .roles import Role
from domain.desk.announcement import Announcement
from .user import User


class Admin(Employee):
    def __init__(self, uid: int, username: str, password: str):
        super(Employee, self).__init__(uid, username, password, Role.ADMIN)

    def post_announcement(self, announcement: Announcement) -> None:
        pass

    def add_user(self, user: User) -> None:
        pass

from flask_login import UserMixin
from . import Base
from sqlalchemy import Column, Integer, String, Enum
from domain.users.roles import Role
from api import dbconn


class DBUser(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    password = Column(String(30), unique=False, nullable=False)
    role = Column(Enum(Role), nullable=False)

    @staticmethod
    def check_user(i_username, i_password) -> bool:
        user = DBUser.get_user(name=i_username)
        return bool(user) and user.password == i_password

    @staticmethod
    def get_user(**kwargs):
        with open(dbconn) as s:
            user = s.query(DBUser).filter_by(**kwargs).first()

        return user

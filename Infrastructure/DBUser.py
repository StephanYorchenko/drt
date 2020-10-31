from flask_login import UserMixin
from Infrastructure import Base
from sqlalchemy import Column, Integer, String, Enum
from Domain.Users.Roles import Role
from api import db_session


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
        s = db_session()
        user = s.query(DBUser).filter_by(**kwargs).first()
        s.close()
        return user

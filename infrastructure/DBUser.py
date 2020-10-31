from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, Boolean
from api import db_session

Base = declarative_base()


class DBUser(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    password = Column(String(30), unique=False, nullable=False)
    educated = Column(Boolean)
    admin = Column(Boolean)
    task = Column(Integer)

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

from flask_login import UserMixin
from infrastructure import Base
from sqlalchemy import Column, Integer, String, Enum
from infrastructure.database_manager import dbconn, db_session
import hashlib


class DBUser(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), unique=True, nullable=False)
    user_hash = Column(String(30), unique=False, nullable=False)
    role = Column(String, nullable=False)

    @staticmethod
    def check_user(i_username: str, i_hash: str) -> bool:
        user = DBUser.get_user(name=i_username)
        return bool(user) and user.user_hash == i_hash

    @staticmethod
    def update_user_hash(i_username: str, new_hash) -> None:
        with dbconn as session:
            session.query(DBUser).filter_by(name=i_username).update(
                {DBUser.user_hash: new_hash})

    @staticmethod
    def get_user(**kwargs):
        with dbconn as session:
            user = session.query(DBUser).filter_by(**kwargs).first()

        return user

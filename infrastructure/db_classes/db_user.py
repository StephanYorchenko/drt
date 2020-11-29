from flask_login import UserMixin
from infrastructure import Base
from sqlalchemy import Column, Integer, String, Enum
from domain.users.roles import Role
from infrastructure.database_manager import dbconn


class DBUser(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    user_hash = Column(String(30), unique=False, nullable=False)
    role = Column(Enum(Role), nullable=False)

    @staticmethod
    def check_user(i_username: str, i_hash: str) -> bool:
        user = DBUser.get_user(name=i_username)
        return bool(user) and user.user_hash == i_hash

    @staticmethod
    def update_user_hash(i_username: str, new_hash) -> None:
        with dbconn as conn:
            user = conn.query(DBUser).filter_by(name=i_username).first()
            user.user_hash = new_hash
            conn.commit()

    @staticmethod
    def get_user(**kwargs):
        with dbconn as conn:
            user = conn.query(DBUser).filter_by(**kwargs).first()

        return user

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from infrastructure import Base
from infrastructure.database_manager import dbconn
from infrastructure.db_records.user_record import UserRecord


class DBUser(UserMixin, Base):
    # noinspection SpellCheckingInspection
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
            user = session.query(DBUser).filter_by(name=i_username)
            user.update({DBUser.user_hash: new_hash})

    @staticmethod
    def update_username(user_id: int, new_username):
        with dbconn as session:
            user = session.query(DBUser).filter_by(id=user_id)
            user.update({DBUser.name: new_username})

    @staticmethod
    def update_password(user_id: int, new_password: str):
        with dbconn as session:
            user = session.query(DBUser).filter_by(id=user_id)
            user.update({DBUser.password: new_password})

    @staticmethod
    def update_role(user_id: int, new_role: str):
        if new_role.lower() not in ('admin', 'hostess', 'employee'):
            raise ValueError('Role is not correct')

        with dbconn as session:
            user = session.query(DBUser).filter_by(id=user_id)
            user.update({DBUser.role: new_role})

    @staticmethod
    def get_db_user(**kwargs):
        with dbconn as session:
            user = session.query(DBUser).filter_by(**kwargs).first()

        return user

    @staticmethod
    def get_user(**kwargs):
        return UserRecord.from_db_type(DBUser.get_db_user(**kwargs))

    @staticmethod
    def add_user(**kwargs):
        if kwargs['role'].lower() not in ('admin', 'hostess', 'employee'):
            raise ValueError

        with dbconn as session:
            new_user = DBUser(
                name=kwargs['name'],
                password=kwargs['password'],
                role=kwargs['role']
            )
            session.add(new_user)

    @staticmethod
    def get_all():
        with dbconn as session:
            users = session.query(DBUser).all()

        return [UserRecord.from_db_type(user) for user in users]

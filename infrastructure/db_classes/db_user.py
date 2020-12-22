from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
from infrastructure import Base
from infrastructure.database_manager.dblink import DBConn
from infrastructure.db_records.user_record import UserRecord
# from ..database_manager.dblink import db_engine


class _DBUser(UserMixin, Base):
    # noinspection SpellCheckingInspection
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), unique=True, nullable=False)
    user_hash = Column(String(30), unique=False, nullable=False)
    role = Column(Integer, nullable=False)

    def __init__(self, dbconn: DBConn, engine: Engine):
        self.dbconn = dbconn
        self.engine = engine

    def check_user(self, i_username: str, i_hash: str) -> bool:
        user = self.get_user(name=i_username)
        return bool(user) and user.user_hash == i_hash

    def update_user_hash(self, i_username: str, new_hash) -> None:
        with self.dbconn as session:
            user = session.query(_DBUser).filter_by(name=i_username)
            user.update({_DBUser.user_hash: new_hash})

    def update_username(self, user_id: int, new_username):
        with self.dbconn as session:
            user = session.query(_DBUser).filter_by(id=user_id)
            user.update({_DBUser.name: new_username})

    def update_password(self, user_id: int, new_password: str):
        with self.dbconn as session:
            user = session.query(_DBUser).filter_by(id=user_id)
            user.update({_DBUser.password: new_password})

    def update_role(self, user_id: int, new_role: int):
        with self.dbconn as session:
            user = session.query(_DBUser).filter_by(id=user_id)
            user.update({_DBUser.role: new_role})

    def get_db_user(self, **kwargs):
        with self.dbconn as session:
            user = session.query(_DBUser).filter_by(**kwargs).first()

        return user

    def get_user(self, **kwargs):
        return UserRecord.from_db_type(self.get_db_user(**kwargs))

    def add_user(self, **kwargs):
        session = Session(self.engine)
        new_user = _DBUser(self.dbconn, self.engine)

        new_user.name = kwargs['name']
        new_user.password = kwargs['password']
        new_user.role = kwargs['role']

        session.add(new_user)
        session.commit()
        session.close()

    def get_all(self):
        with self.dbconn as session:
            users = session.query(_DBUser).all()

        return [UserRecord.from_db_type(user) for user in users]

    def delete_user(self, **kwargs):
        session = Session(self.engine)
        user = self.get_db_user(**kwargs)

        session.delete(user)
        session.commit()
        session.close()


class DBUser:
    def __init__(self, dbconn: DBConn, engine: Engine):
        self.db_user = _DBUser(dbconn, engine)

    def check_user(self, i_username: str, i_hash: str) -> bool:
        return self.db_user.check_user(i_username, i_hash)

    def update_user_hash(self, i_username: str, new_hash) -> None:
        return self.db_user.update_user_hash(i_username, new_hash)

    def update_username(self, user_id: int, new_username):
        return self.db_user.update_username(user_id, new_username)

    def update_password(self, user_id: int, new_password: str):
        return self.db_user.update_password(user_id, new_password)

    def update_role(self, user_id: int, new_role: int):
        return self.db_user.update_role(user_id, new_role)

    def get_db_user(self, **kwargs):
        return self.db_user.get_db_user(**kwargs)

    def get_user(self, **kwargs):
        return self.db_user.get_user(**kwargs)

    def add_user(self, **kwargs):
        return self.db_user.add_user(**kwargs)

    def get_all(self):
        return self.db_user.get_all()

    def delete_user(self, **kwargs):
        return self.db_user.delete_user(**kwargs)

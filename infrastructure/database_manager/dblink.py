from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from ..config import Config


class DBConn:
    def __init__(self, db: Session):
        self.db = db

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()


def db_session():
    return db.bdsession


def db_engine():
    return db.engine


class Db(object):
    def __init__(self, test=False):
        self.test = test
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        self.bdsession = sessionmaker(bind=self.engine, autocommit=True)()
        self.connect = self.engine.connect()


db = Db()
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
bdsession = sessionmaker(bind=engine, autocommit=True)()
dbconn = DBConn(bdsession)

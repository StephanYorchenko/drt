from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..config import Config


class DBConn:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        return self.db.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("AAAAAAAAAAA")
        print(dir(self.db))
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
dbconn = DBConn(db)

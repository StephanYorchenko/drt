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


class Db(object):
    def __init__(self, test=False):
        self.test = test
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        self.bdsession = sessionmaker(bind=self.engine, autocommit=True)()
        self.connect = self.engine.connect()

from datetime import datetime

from sqlalchemy import Column, Integer, Text, String, Boolean
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from infrastructure import Base
from infrastructure.database_manager.dblink import DBConn
from infrastructure.db_records.request_record import RequestRecord


class DBTableRequest(Base):
    # noinspection SpellCheckingInspection
    __tablename__ = 'request_table'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    date = Column(String)
    username = Column(String, nullable=False)

    def __init__(self, dbconn: DBConn, engine: Engine):
        self.dbconn = dbconn
        self.engine = engine

    def get(self):
        with self.dbconn as session:
            new_table_requests = session.query(DBTableRequest).all()

        return new_table_requests
        # return list(map(RequestRecord.from_db_type, requests))

    def add(self, record):
        session = Session(self.engine)
        new_table_request = DBTableRequest(self.dbconn, self.engine)

        new_table_request.number = record.topic
        new_table_request.username = record.username
        new_table_request.date = record.date

        session.add(new_table_request)
        session.commit()
        session.close()

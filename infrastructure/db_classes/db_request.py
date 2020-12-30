from datetime import datetime

from sqlalchemy import Column, Integer, Text, ForeignKey, String, Boolean
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from infrastructure import Base
from infrastructure.database_manager.dblink import DBConn
from infrastructure.db_records.request_record import RequestRecord
from infrastructure.engine_wrapper import EngineWrapper


class _DBRequest(Base):
    # noinspection SpellCheckingInspection
    __tablename__ = 'request'

    id = Column(Integer, primary_key=True)
    comment = Column(Text, nullable=True)
    topic = Column(String, nullable=True)
    approved = Column(Boolean, default=False)
    date = Column(String, default=datetime.now)
    username = Column(String, nullable=False)

    def __init__(self, dbconn: DBConn, engine: Engine):
        self.dbconn = dbconn
        self.engine = engine

    def get(self):
        with self.dbconn as session:
            requests = session.query(_DBRequest).all()

        return list(map(RequestRecord.from_db_type, requests))

    def change_approval(self, request_id: int, approved: bool):
        with self.dbconn as session:
            user = session.query(_DBRequest).filter_by(id=request_id)
            user.update({_DBRequest.approved: approved})

    def add(self, record: RequestRecord):
        session = Session(self.engine)
        new_request = _DBRequest(self.dbconn, self.engine)

        new_request.approved = record.approved
        new_request.topic = record.topic
        new_request.comment = record.comment
        new_request.username = record.username
        new_request.date = record.date

        session.add(new_request)
        session.commit()
        session.close()


class DBRequest:
    def __init__(self, dbconn: DBConn, engine: EngineWrapper):
        self.db_request = _DBRequest(dbconn, engine.engine)

    def get(self):
        return self.db_request.get()

    def change_approval(self, request_id: int, approved: bool):
        return self.db_request.change_approval(request_id, approved)

    def add(self, record: RequestRecord):
        self.db_request.add(record)

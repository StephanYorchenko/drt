from datetime import datetime

from sqlalchemy import Column, Integer, Text, ForeignKey, String, Boolean
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from infrastructure import Base
from infrastructure.database_manager.dblink import DBConn
from infrastructure.db_records.request_record import RequestRecord


class DBRequest(Base):
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
            requests = session.query(DBRequest).all()

        return list(map(RequestRecord, requests))

    def change_approval(self, request_id: int, is_watched: bool):
        with self.dbconn as session:
            user = session.query(DBRequest).filter_by(id=request_id)
            user.update({DBRequest.approved: is_watched})

    def add(self, record: RequestRecord):
        session = Session(self.engine)
        new_request = DBRequest(self.dbconn, self.engine)

        new_request.approved = record.approved
        new_request.topic = record.topic
        new_request.comment = record.comment
        new_request.user_id = record.user_id
        new_request.date = record.date

        session.add(new_request)
        session.commit()
        session.close()

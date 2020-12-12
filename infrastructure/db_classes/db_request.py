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
    is_watched = Column(Boolean, default=False)
    date = Column(String, default=datetime.now)
    user_id = Column(Integer, nullable=False)

    def __init__(self, dbconn: DBConn, engine: Engine):
        self.dbconn = dbconn
        self.engine = engine

    def get(self):
        with self.dbconn as session:
            requests = session.query(DBRequest).all()

        return list(map(RequestRecord, requests))

    def update_watched(self, request_id: int, is_watched: bool):
        with self.dbconn as session:
            user = session.query(DBRequest).filter_by(id=request_id)
            user.update({DBRequest.is_watched: is_watched})

    def add(self, **kwargs):
        session = Session(self.engine)
        new_request = DBRequest(self.dbconn, self.engine)

        new_request.is_watched = kwargs['is_watched']
        new_request.topic = kwargs['topic']
        new_request.comment = kwargs['comment']
        new_request.user_id = kwargs['user_id']
        new_request.date = kwargs['date']

        session.add(new_request)
        session.commit()
        session.close()

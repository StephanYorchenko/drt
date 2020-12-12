from datetime import datetime

from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from infrastructure import Base
from infrastructure.database_manager.dblink import DBConn
from infrastructure.db_records.announcement_record import AnnouncementRecord


class DBAnnouncement(Base):
    # noinspection SpellCheckingInspection
    __tablename__ = 'announcement'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=True)
    title = Column(String, nullable=True)
    date = Column(String, default=datetime.now)
    # user_id = Column(Integer, nullable=False)

    def __init__(self, dbconn: DBConn, engine: Engine):
        self.dbconn = dbconn
        self.engine = engine

    def get(self):
        with self.dbconn as session:
            announcements = session.query(DBAnnouncement).all()

        return [AnnouncementRecord.from_db_type(announcement)
                for announcement in announcements]

    def add(self, **kwargs):
        session = Session(self.engine)
        new_announcement = DBAnnouncement(self.dbconn, self.engine)

        new_announcement.text = kwargs['text']
        new_announcement.title = kwargs['title']
        new_announcement.date = kwargs['date']

        session.add(new_announcement)
        session.commit()
        session.close()

from datetime import datetime

from sqlalchemy import Column, Integer, Text, String

from infrastructure import Base
from infrastructure.database_manager import dbconn
from infrastructure.db_records.announcement_record import AnnouncementRecord


class DBAnnouncement(Base, ):
    # noinspection SpellCheckingInspection
    __tablename__ = 'announcement'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=True)
    title = Column(String, nullable=True)
    date = Column(String, default=datetime.now)
    # user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'),
    #                  nullable=False)

    @staticmethod
    def get():
        with dbconn as session:
            announcements = session.query(DBAnnouncement).all()

        return [AnnouncementRecord.from_db_type(announcement)
                for announcement in announcements]

    @staticmethod
    def add(**kwargs):
        with dbconn as session:
            announcement = DBAnnouncement(kwargs['user_id'],
                                          kwargs['text'],
                                          kwargs['title'])
            session.add(announcement)

        return announcement

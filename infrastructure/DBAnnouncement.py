from sqlalchemy import Column, Integer, Text, ForeignKey, String, DateTime
from infrastructure import Base
from api import dbconn
from datetime import datetime


class DBAnnouncement(Base):
    __tablename__ = 'announcement'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=True)
    topic = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    @staticmethod
    def get_announcements():
        with open(dbconn) as s:
            announcements = s.query(DBAnnouncement).all()

        return announcements

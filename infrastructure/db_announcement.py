from sqlalchemy import Column, Integer, Text, ForeignKey, String, DateTime
from infrastructure import Base
from api import dbconn, db_session
from datetime import datetime


class DBAnnouncement(Base):
    __tablename__ = 'announcement'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=True)
    title = Column(String, nullable=True)
    date = Column(String, default=datetime.now)
    # user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'),
    #                  nullable=False)

    @staticmethod
    def get():
        # with dbconn as s:
        #     announcements = s.query(DBAnnouncement).all()
        s = db_session()
        announcements = s.query(DBAnnouncement).all()
        s.close()

        # return announcements
        return [dict(
            id=announcement.id,
            text=announcement.text,
            title=announcement.title,
            date=announcement.date,
        ) for announcement in announcements]

    @staticmethod
    def add(**kwargs):
        with dbconn as s:
            announcement = DBAnnouncement(kwargs['user_id'], kwargs['text'],
                                          kwargs['title'])
            s.add(announcement)

        return announcement

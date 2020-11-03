from sqlalchemy import Column, Integer, Text, String
from infrastructure import Base
from application.api import dbconn, db_session
from datetime import datetime


class DBAnnouncement(Base, ):
    __tablename__ = 'announcement'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=True)
    title = Column(String, nullable=True)
    date = Column(String, default=datetime.now)
    # user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'),
    #                  nullable=False)

    @staticmethod
    def to_json(announcement):
        return dict(
            id=announcement.id,
            text=announcement.text,
            title=announcement.title,
            date=announcement.date,
        )

    @staticmethod
    def get():
        s = db_session()
        announcements = s.query(DBAnnouncement).all()
        s.close()

        return [DBAnnouncement.to_json(announcement) for announcement in announcements]

    @staticmethod
    def add(**kwargs):
        with dbconn as conn:
            announcement = DBAnnouncement(kwargs['user_id'],
                                          kwargs['text'],
                                          kwargs['title'])
            conn.add(announcement)

        return announcement

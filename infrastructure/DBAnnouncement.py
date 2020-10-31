from sqlalchemy import Column, Integer, Text, ForeignKey, String, DateTime
from infrastructure import Base
from api import dbconn


class DBAnnouncement(Base):
    __tablename__ = 'announcement'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=True)
    topic = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    # @staticmethod
    # def check_user(i_username, i_password) -> bool:
    #     user = DBAnnouncement.get_user(name=i_username)
    #     return bool(user) and user.password == i_password

    @staticmethod
    def get_announcements():
        return "lol"
from sqlalchemy import Column, Integer, Text, ForeignKey, String
from infrastructure import Base


class DBAnnouncement(Base):
    __tablename__ = 'announcement'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=True)
    topic = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

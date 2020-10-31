from sqlalchemy import Column, Integer, Text, ForeignKey, String, Boolean
from infrastructure import Base


class Request(Base):
    __table_name__ = 'request'

    id = Column(Integer, primary_key=True)
    comment = Column(Text, nullable=True)
    topic = Column(String, nullable=True)
    is_watched = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

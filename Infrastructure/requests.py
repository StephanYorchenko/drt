from sqlalchemy import Column, Integer, Text, ForeignKey
from Infrastructure import Base


class Request(Base):
    __table_name__ = 'request'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

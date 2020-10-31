from sqlalchemy import Column, Integer, Text, ForeignKey, String
from infrastructure import Base


class Request(Base):
    __table_name__ = 'request'

    id = Column(Integer, primary_key=True)
    comment = Column(Text, nullable=True)
    type = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

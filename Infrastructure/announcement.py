from sqlalchemy import Column, Integer, Text, ForeignKey
from Infrastructure import Base


class Announcement(Base):
    __tablename__ = 'announcement'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

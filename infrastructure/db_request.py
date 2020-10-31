from sqlalchemy import Column, Integer, Text, ForeignKey, String, Boolean
from infrastructure import Base
from api import dbconn


class DBRequest(Base):
    __table_name__ = 'request'

    id = Column(Integer, primary_key=True)
    comment = Column(Text, nullable=True)
    topic = Column(String, nullable=True)
    is_watched = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'),
                     nullable=False)

    @staticmethod
    def get():
        with dbconn as c:
            requests = c.query(DBRequest).all()

        return requests

    @staticmethod
    def add(**kwargs):
        with dbconn as c:
            c.add(DBRequest(kwargs['id'], kwargs['comment'], kwargs['type'],
                            kwargs['user_id']))
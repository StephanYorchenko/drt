from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from infrastructure.db_classes.db_user import DBUser
from infrastructure.db_classes.db_announcement import DBAnnouncement
from infrastructure.db_classes.db_request import DBRequest
from infrastructure.db_records.request_record import RequestRecord
from infrastructure.db_records.user_record import UserRecord
from .db_records.announcement_record import AnnouncementRecord

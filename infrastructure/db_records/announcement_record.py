from dataclasses import dataclass
from typing import Dict

from infrastructure.db_classes.db_announcement import DBAnnouncement


@dataclass
class AnnouncementRecord:
    title: str
    text: str
    user_id: int
    date: str

    @staticmethod
    def from_db_type(announcement: DBAnnouncement):
        return AnnouncementRecord(announcement.title, announcement.text,
                                  announcement.id, announcement.date)

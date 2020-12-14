from dataclasses import dataclass


@dataclass
class AnnouncementRecord:
    title: str
    text: str
    date: str

    @staticmethod
    def from_db_type(announcement):
        return AnnouncementRecord(
            announcement.title,
            announcement.text,
            announcement.date
        )

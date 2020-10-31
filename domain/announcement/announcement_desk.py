import typing
from domain.announcement.announcement import Announcement
from infrastructure.db_announcement import DBAnnouncement
from domain.desk import Desk


ANNOUNCEMENT_COUNT = 15


class AnnouncementDesk(Desk):
    @staticmethod
    def get(page):
        if page < 1:
            raise ValueError("Incorrect page number")
        jsons = DBAnnouncement.get()
        try:
            return list(map(lambda data: Announcement.from_json(data),
                            jsons[(page - 1) * ANNOUNCEMENT_COUNT:
                                  min(page * ANNOUNCEMENT_COUNT,
                                      len(jsons))]))
        except IndexError:
            return []

    @staticmethod
    def add(announcement):
        DBAnnouncement.add(topic=announcement.topic, text=announcement.text,
                           user_id=announcement.user_id)

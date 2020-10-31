import typing
from domain.desk.announcement import Announcement
from infrastructure.DBAnnouncement import DBAnnouncement


ANNOUNCEMENT_COUNT = 15


class Desk:
    @staticmethod
    def get_announcements(page) -> typing.List[Announcement]:
        if page < 1:
            raise ValueError("Incorrect page number")
        jsons = DBAnnouncement.get_announcements()
        try:
            return list(map(lambda data: Announcement.from_json(data),
                            jsons[(page - 1) * ANNOUNCEMENT_COUNT:
                                  min(page * ANNOUNCEMENT_COUNT, len(jsons))]))
        except IndexError:
            return []

    @staticmethod
    def add_announcement(announcement):
        ann = DBAnnouncement(announcement.id, announcement.text,
                             announcement.topic)
        ann.add(topic=announcement.topic, text=announcement.text,
                user_id=announcement.user_id)

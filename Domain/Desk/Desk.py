import typing

from Domain.Desk.Announcement import Announcement
from infrastructure.DBAnnouncement import DBAnnouncement


class Desk:
    def __init__(self):
        pass

    @staticmethod
    def get_announcements(n) -> typing.List[Announcement]:
        jsons = DBAnnouncement.get_announcements()[:n]
        return list(map(lambda data: Announcement.from_json(data), jsons))

    def add_announcement(self):
        pass

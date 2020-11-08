import typing
from domain.announcement.announcement import Announcement
from infrastructure.db_announcement import DBAnnouncement
from domain.desk import Desk


ANNOUNCEMENT_COUNT = 7


class AnnouncementDesk(Desk):
    def __init__(self):
        super(AnnouncementDesk, self).__init__(Announcement, DBAnnouncement,
                                               ANNOUNCEMENT_COUNT)

from domain.announcement.announcement import Announcement
from infrastructure.db_announcement import DBAnnouncement
from application.domain_serializers.announcement_serializer import \
    AnnouncementSerializer
from application.desks.desk import Desk

ANNOUNCEMENT_COUNT = 7


class AnnouncementDesk(Desk):
    def __init__(self):
        super(AnnouncementDesk, self).__init__(Announcement, DBAnnouncement,
                                               AnnouncementSerializer(),
                                               ANNOUNCEMENT_COUNT)

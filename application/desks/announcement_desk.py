from application.desks.desk import Desk
from application.domain_serializers.announcement_serializer import AnnouncementSerializer
from infrastructure.db_classes.db_announcement import DBAnnouncement

ANNOUNCEMENT_COUNT = 7


class AnnouncementDesk(Desk):
    def __init__(self):
        super(AnnouncementDesk, self).__init__(DBAnnouncement, AnnouncementSerializer(), ANNOUNCEMENT_COUNT)

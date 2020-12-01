from application.desks.desk import Desk
from application.record_transformer.announcement_transformer \
    import AnnouncementTransformer
from infrastructure.db_classes.db_announcement import DBAnnouncement

ANNOUNCEMENT_COUNT = 7


class AnnouncementDesk(Desk):
    def __init__(self):
        super(AnnouncementDesk, self).__init__(DBAnnouncement,
                                               AnnouncementTransformer(),
                                               ANNOUNCEMENT_COUNT)

from domain.announcement.announcement import Announcement
from .domain_transformer import DomainTransformer


class AnnouncementTransformer(DomainTransformer):
    def __init__(self):
        super().__init__(lambda record:
                         Announcement(record.title, record.text,
                                      record.user_id, record.date))

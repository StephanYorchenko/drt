from application.providers.provider import Provider
from application.transformers import AnnouncementTransformer
from application.filters import AnnouncementFilter
from infrastructure import DBAnnouncement


class AnnouncementProvider(Provider):
    def __init__(self,
                 db_entry_type: DBAnnouncement,
                 transformer: AnnouncementTransformer,
                 filter: AnnouncementFilter,
                 entry_count):
        super().__init__(db_entry_type, transformer, filter, entry_count)

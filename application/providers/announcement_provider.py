from application.providers.provider import Provider
from application.transformers import AnnouncementRecordTransformer
from application.filters import AnnouncementFilter
from infrastructure import DBAnnouncement


class AnnouncementProvider(Provider):
    def __init__(self,
                 db_entry_type: DBAnnouncement,
                 transformer: AnnouncementRecordTransformer,
                 filter: AnnouncementFilter,
                 entry_count):
        super().__init__(db_entry_type, transformer, filter, entry_count)

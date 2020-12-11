from application.providers.provider import Provider
from application.transformers import AnnouncementTransformer
from infrastructure import DBAnnouncement


class AnnouncementProvider(Provider):
    def __init__(self,
                 db_entry_type: DBAnnouncement,
                 transformer: AnnouncementTransformer,
                 entry_count):
        super().__init__(db_entry_type, transformer, entry_count)

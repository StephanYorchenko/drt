from typing import Tuple

from application.providers.provider import Provider
from application.transformers import AnnouncementRecordTransformer
from application.filters import AnnouncementFilter
from application.user_manager import UserManager
from domain import Role
from infrastructure import DBAnnouncement


class AnnouncementProvider(Provider):
    def __init__(self,
                 db_entry_type: DBAnnouncement,
                 transformer: AnnouncementRecordTransformer,
                 filter: AnnouncementFilter,
                 user_manager: UserManager,
                 entry_count):
        super().__init__(db_entry_type, transformer, filter, user_manager,
                         entry_count)

    def check_rights(self, username, *roles):
        super(AnnouncementProvider, self).check_rights(username, *roles)

    def get(self, page, caller_name) -> Tuple[list, int]:
        self.check_rights(caller_name, Role.ADMIN, Role.HOSTESS, Role.EMPLOYEE)
        res = super(AnnouncementProvider, self).get(page, caller_name)
        return res

    def add(self, entry, caller_name):
        self.check_rights(caller_name, Role.ADMIN)
        return super(AnnouncementProvider, self).add(entry, caller_name)

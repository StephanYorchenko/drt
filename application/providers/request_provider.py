from application.filters import RequestFilter
from application.providers.provider import Provider
from application.transformers import RequestRecordTransformer
from application.user_manager import UserManager
from domain import Role
from infrastructure import DBRequest


class RequestProvider(Provider):
    def __init__(self,
                 db_entry_type: DBRequest,
                 transformer: RequestRecordTransformer,
                 filter: RequestFilter,
                 user_manager: UserManager,
                 entry_count):
        super().__init__(db_entry_type, transformer, filter, user_manager,
                         entry_count)

    def check_rights(self, username, *roles):
        super(RequestProvider, self).check_rights(username, *roles)

    def get_all(self, caller_name) -> list:
        self.check_rights(caller_name, Role.HOSTESS)
        return super(RequestProvider, self).get_all(caller_name)

    def add(self, entry, caller_name):
        self.check_rights(caller_name, Role.EMPLOYEE, Role.ADMIN, Role.HOSTESS)
        print(entry)
        return super(RequestProvider, self).add(entry, caller_name)

    def change_approval(self, request_id: int, value: bool, caller_name: str):
        self.check_rights(caller_name, Role.HOSTESS)
        self._db_entry_type.change_approval(request_id, value)

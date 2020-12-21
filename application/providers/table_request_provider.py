from application.filters import TableRequestFilter
from application.providers.provider import Provider
from application.transformers import TableRequestRecordTransformer
from application.user_manager import UserManager
from domain import Role, TableRequest
from infrastructure import DBTableRequest


class TableRequestProvider(Provider):
    def __init__(self,
                 db_entry_type: DBTableRequest,
                 transformer: TableRequestRecordTransformer,
                 filter: TableRequestFilter,
                 user_manager: UserManager,
                 entry_count: int = 7):
        super().__init__(db_entry_type, transformer, filter, user_manager,
                         entry_count)

    def check_rights(self, username, *roles):
        super(TableRequestProvider, self).check_rights(username, *roles)

    def get_all(self, caller_name, internal=False) -> list:
        if not internal:
            self.check_rights(caller_name, Role.ADMIN)
        return super(TableRequestProvider, self).get_all(caller_name)

    def try_book(self, number: int, date: str, caller_name: str):
        self.check_rights(caller_name, Role.ADMIN, Role.EMPLOYEE)
        requests = self.get_all(caller_name, True)
        for request in requests:
            if request.number == number and request.date == date:
                return dict(
                    result=False
                )
        self._db_entry_type.add(
            self.transformer.to_record(TableRequest(
                0,
                number,
                date,
                caller_name
            )))
        return dict(
            result=True
        )

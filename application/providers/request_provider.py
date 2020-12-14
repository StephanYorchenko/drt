from application.providers.provider import Provider
from application.transformers import RequestRecordTransformer
from application.filters import RequestFilter
from domain import Request
from infrastructure import DBRequest


class RequestProvider(Provider):
    def __init__(self,
                 db_entry_type: DBRequest,
                 transformer: RequestRecordTransformer,
                 filter: RequestFilter,
                 entry_count):
        super().__init__(db_entry_type, transformer, filter, entry_count)

    def change_approval(self, request_id: int, value: bool):
        self._db_entry_type.change_approval(request_id, value)

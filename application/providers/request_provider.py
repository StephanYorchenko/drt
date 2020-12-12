from application.providers.provider import Provider
from application.transformers import RequestTransformer
from application.filters import RequestFilter
from infrastructure import DBRequest


class RequestProvider(Provider):
    def __init__(self,
                 db_entry_type: DBRequest,
                 transformer: RequestTransformer,
                 filter: RequestFilter,
                 entry_count):
        super().__init__(db_entry_type, transformer, filter, entry_count)


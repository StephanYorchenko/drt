from .desk import Desk
from ui.transformers.table_request_json_transformer import\
    TableRequestJsonTransformer
from application import TableRequestProvider


class TableRequestDesk(Desk):
    def __init__(self, provider: TableRequestProvider,
                 transformer: TableRequestJsonTransformer,
                 name=''):
        super(TableRequestDesk, self).__init__(
            provider,
            transformer,
            name
        )

    def try_book(self, table_number: int, date: str):
        return self.provider.try_book(
            table_number, date, super().get_caller_name())

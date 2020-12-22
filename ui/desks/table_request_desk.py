from flask import request

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

    def try_book(self):
        number = int(request.form.get('number'))
        date = request.form.get('date')
        username = request.form.get('username')
        return self.provider.try_book(
            number, date, username)

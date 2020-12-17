from flask import request

from ui.desks.desk import Desk
from ui.transformers import RequestJsonTransformer
from application import RequestProvider


class RequestDesk(Desk):
    def __init__(self, provider: RequestProvider,
                 transformer: RequestJsonTransformer, name: str):
        super().__init__(provider, transformer, name)

    def change_approval(self):
        self.provider.change_approval(request.form['id'], True,
                                      super().get_caller_name())
        return 'Success'

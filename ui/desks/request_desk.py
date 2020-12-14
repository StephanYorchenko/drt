from flask import request

from ui.desks.desk import Desk
from ui.transformers import RequestJsonTransformer
from application import RequestProvider


class RequestDesk(Desk):
    def __init__(self, provider: RequestProvider,
                 transformer: RequestJsonTransformer, name: str):
        super().__init__(provider, transformer, name)

    def change_approval(self):
        data = request.form
        # json = dict()
        # for key in list(data.keys()):
        #     json[key] = data[key]
        print(list(data.keys()), "AAAAAAAAAAAAAAAAAAAAAaa")

        self.provider.change_approval(data['request_id'], True)

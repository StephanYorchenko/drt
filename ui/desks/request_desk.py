from ui.desks.desk import Desk
from application import RequestProvider


class RequestDesk(Desk):
    def __init__(self, provider: RequestProvider, name: str):
        super().__init__(provider, name)

    def change_approval(self, request_id: int, value: bool):
        # noinspection PyUnresolvedReferences
        self.provider.change_approval(request_id, value)

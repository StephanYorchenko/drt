from ui.routes.desks.desk import Desk
from application import RequestProvider


class RequestDesk(Desk):
    def __init__(self, provider: RequestProvider, name: str):
        super().__init__(provider, name)

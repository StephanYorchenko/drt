from domain.desk import Desk
from .request import Request
from infrastructure.db_request import DBRequest


REQUEST_COUNT = 10


class RequestDesk(Desk):
    def __init__(self):
        super().__init__(Request, DBRequest, REQUEST_COUNT)

from application.desks.desk import Desk
from domain.request.request import Request
from infrastructure.db_request import DBRequest
from application.domain_serializers.request_serializer import RequestSerializer


REQUEST_COUNT = 10


class RequestDesk(Desk):
    def __init__(self):
        super().__init__(Request, DBRequest, RequestSerializer(),
                         REQUEST_COUNT)

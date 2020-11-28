from application.desks.desk import Desk
from application.domain_serializers.request_serializer import RequestSerializer
from infrastructure.db_classes.db_request import DBRequest

REQUEST_COUNT = 10


class RequestDesk(Desk):
    def __init__(self):
        super().__init__(DBRequest, RequestSerializer(), REQUEST_COUNT)

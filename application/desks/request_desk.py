from application.desks.desk import Provider
from application.record_transformer.request_transformer \
    import RequestTransformer
from infrastructure.db_classes.db_request import DBRequest

REQUEST_COUNT = 10


class RequestProvider(Provider):
    def __init__(self):
        super().__init__(DBRequest, RequestTransformer(), REQUEST_COUNT)

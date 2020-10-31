from domain.desk import Desk
from .request import Request
from infrastructure.db_request import DBRequest


REQUEST_COUNT = 10


class RequestDesk(Desk):
    @staticmethod
    def get(page):
        if page < 1:
            raise ValueError("Incorrect page number")
        jsons = DBRequest.get()
        try:
            return list(map(lambda data: Request.from_json(),
                            jsons[(page - 1) * REQUEST_COUNT:
                                  min(page * REQUEST_COUNT,
                                      len(jsons))]))
        except IndexError:
            return []

    @staticmethod
    def add(request):
        DBRequest.add(**request.to_json())

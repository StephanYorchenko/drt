from domain.desk import Desk
from .request import Request
from infrastructure.DBRequests import DBRequest


REQUEST_COUNT = 10


class RequestDesk(Desk):
    @staticmethod
    def get(page):
        if page < 1:
            raise ValueError("Incorrect page number")
        jsons = DBRequest.get()
        try:
            return list(map(lambda data: Request(data['id'], data['type'],
                                                 data['comment'],
                                                 data['user_id']),
                            jsons[(page - 1) * REQUEST_COUNT:
                                  min(page * REQUEST_COUNT,
                                      len(jsons))]))
        except IndexError:
            return []

    @staticmethod
    def add(request):
        DBRequest.add(id=request.request_id, comment=request.comment,
                      user_id=request.user_id, type=request.request_type)

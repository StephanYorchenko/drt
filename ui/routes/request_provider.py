from application.desks.request_desk import RequestDesk
from .desk_provider import DeskProvider


class RequestProvider(DeskProvider):
    def __init__(self):
        super().__init__(RequestDesk())

    def get(self):
        return self.jsonify_n_serialized_objects_from_desk(
            'requests'
        )
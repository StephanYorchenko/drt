from dataclasses import dataclass

from infrastructure.db_classes.db_request import DBRequest


@dataclass
class RequestRecord:
    request_id: int
    topic: str
    comment: str
    user_id: int
    is_watched: bool

    @staticmethod
    def from_db_type(request: DBRequest):
        return Request(request.id, request.topic, request.comment,
                       request.user_id, request.is_watched)

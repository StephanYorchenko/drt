from dataclasses import dataclass


@dataclass
class RequestRecord:
    id: int
    topic: str
    comment: str
    username: str
    date: str
    approved: bool

    @staticmethod
    def from_db_type(request):
        return RequestRecord(
            request.id,
            request.topic,
            request.comment,
            request.username,
            request.date,
            request.approved
        )

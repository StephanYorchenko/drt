from dataclasses import dataclass


@dataclass
class Request:
    request_id: int
    topic: str
    comment: str
    username: str
    date: str
    approved: bool

    def __eq__(self, other):
        if other is not Request:
            return False
        return self.request_id == other.request_id

import datetime
from domain.users.user import User


class Reservation:
    def __init__(self, user: User, start: datetime, duration: datetime):
        self.user = user
        self.start = start
        self.duration = duration

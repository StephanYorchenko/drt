import datetime
from Domain.Users.User import User


class Reservation:
    def __init__(self, user: User, start: datetime, duration: datetime):
        self.user = user
        self.start = start
        self.duration = duration

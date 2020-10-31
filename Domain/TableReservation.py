import typing
import datetime
from .User import User
from .Table import Table


class Reservation:
    def __init__(self, user: User, start: datetime, duration: datetime):
        self.user = user
        self.start = start
        self.duration = duration

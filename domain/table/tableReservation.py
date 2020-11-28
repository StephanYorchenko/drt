import datetime
from dataclasses import dataclass

from domain.users.user import User


@dataclass
class Reservation:
    user: User
    start: datetime
    duration: datetime

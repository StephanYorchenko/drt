from typing import List
from dataclasses import dataclass

from .tableReservation import Reservation


@dataclass
class Table:
    table_id: int

    def get_reservations(self) -> List[Reservation]:
        pass

    def try_add_reservation(self, reservation: Reservation) -> bool:
        pass

import typing
from .tableReservation import Reservation


class Table:
    def __init__(self, table_id: int):
        self.id = table_id

    def get_reservations(self) -> typing.List[Reservation]:
        pass

    def try_add_reservation(self, reservation: Reservation) -> bool:
        pass

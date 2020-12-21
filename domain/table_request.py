from dataclasses import dataclass


@dataclass
class TableRequest:
    id: int
    table_number: int
    date: str
    username: str

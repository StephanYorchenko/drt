from dataclasses import dataclass


@dataclass
class TableRequest:
    id: int
    number: int
    date: str
    username: str


from dataclasses import dataclass

from infrastructure.db_classes.db_table_request import DBTableRequest


@dataclass
class TableRequestRecord:
    id: int
    table_number: int
    date: str
    username: str

    @staticmethod
    def from_db_type(table_request: DBTableRequest):
        return TableRequestRecord(
            table_request.id,
            table_request.number,
            table_request.date,
            table_request.username)

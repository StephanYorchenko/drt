import abc
from infrastructure.serializable import Serializable


class Desk(abc.ABC):
    def __init__(self, entry_type, db_entry_type,
                 entry_count: int):
        self._entry_type = entry_type
        self._entry_count = entry_count
        self._db_entry_type = db_entry_type

    def get(self, page) -> list:
        if page < 1:
            raise ValueError("Incorrect page number")
        jsons = self._db_entry_type.get()
        try:
            return list(map(lambda data: self._entry_type.from_json(data),
                            jsons[(page - 1) * self._entry_count:
                                  min(page * self._entry_count,
                                      len(jsons))]))
        except IndexError:
            return []

    def add(self, entry: Serializable):
        self._db_entry_type.add(**entry.to_json())

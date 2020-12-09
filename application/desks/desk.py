import abc
from typing import Tuple

from application.record_transformer.domain_transformer import DomainTransformer
from infrastructure import DBAnnouncement


class Provider(abc.ABC):
    def __init__(
            self,
            db_entry_type: DBAnnouncement,
            serializer: DomainTransformer,
            entry_count: int = 7
    ):
        self._entry_count = entry_count
        self.serializer = serializer
        self._db_entry_type = db_entry_type

    def get(self, page) -> Tuple[list, int]:
        if page < 1:
            raise ValueError("Incorrect page number")
        jsons = self._db_entry_type.get()
        page_count = (len(jsons) + self._entry_count - 1) // self._entry_count
        try:
            jsons_page = jsons[(page - 1) * self._entry_count:
                               min(page * self._entry_count, len(jsons))]
            return (list(map(lambda data: self.serializer.from_record(data),
                             jsons_page)), page_count)
        except IndexError:
            return [], page_count

    def add(self, entry):
        self._db_entry_type.add(**self.serializer.to_json(entry))

import abc
from typing import Tuple

from application import DomainTransformer
from application.filters import Filter


class Provider(abc.ABC):
    def __init__(
            self,
            db_entry_type,
            transformer,
            filter,
            entry_count: int = 7
    ):
        self._entry_count = entry_count
        self.transformer = transformer
        self.filter = filter
        self._db_entry_type = db_entry_type

    def get(self, page) -> Tuple[list, int]:
        if page < 1:
            raise ValueError("Incorrect page number")
        jsons = self._db_entry_type.get()
        visible = []
        for object in map(self.transformer.from_record, jsons):
            if self.filter(object):
                visible.append(object)
        page_count = (len(visible)
                      + self._entry_count - 1) // self._entry_count
        try:
            page = visible[(page - 1) * self._entry_count:
                               min(page * self._entry_count, len(visible))]
            return page, page_count
        except IndexError:
            return [], page_count

    def add(self, entry):
        self._db_entry_type.add(**self.transformer.to_json(entry))

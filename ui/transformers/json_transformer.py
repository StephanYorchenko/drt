from typing import Dict

from ui.transformers.request_json_transformer import RequestJsonTransformer
from ui.transformers.announcement_json_transfromer \
    import AnnouncementJsonTransformer
from .table_request_json_transformer import TableRequestJsonTransformer


def default_to(obj) -> Dict[str, str]:
    res = {}
    for name, value in obj.__dict__.items():
        if not name.startswith('_'):
            res[name] = value
    return res


class JsonTransformer(AnnouncementJsonTransformer,
                      RequestJsonTransformer,
                      TableRequestJsonTransformer):
    def __init__(self, from_json, to_json=default_to):
        self.from_json = from_json
        self.to_json = to_json

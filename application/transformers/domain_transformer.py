from typing import Dict
from application.transformers.announcement_transformer \
    import AnnouncementTransformer
from application.transformers.request_transformer \
    import RequestTransformer


def default_to(obj) -> Dict[str, str]:
    res = {}
    for name, value in obj.__dict__.items():
        if not name.startswith('_'):
            res[name] = value
    return res


class DomainTransformer(AnnouncementTransformer, RequestTransformer):
    def __init__(self, from_record, to_json=default_to):
        self.from_record = from_record
        self.to_json = to_json

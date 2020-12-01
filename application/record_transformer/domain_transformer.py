from typing import Dict


def default_to(domain_object) -> Dict[str, str]:
    res = {}
    for name, value in domain_object.__dict__.items():
        if not name.startswith('_'):
            res[name] = value
    return res


class DomainTransformer:
    def __init__(self, from_record, to_json=default_to):
        self.from_record = from_record
        self.to_json = to_json

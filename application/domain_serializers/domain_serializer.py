from typing import Dict


def default_to(domain_object) -> Dict[str, str]:
    res = {}
    for name, value in domain_object.__dict__.items():
        if not name.startswith('_'):
            res[name] = value
    return res


class DomainSerializer:
    def __init__(self, from_json, to_json=default_to):
        self.from_json = from_json
        self.to_json = to_json

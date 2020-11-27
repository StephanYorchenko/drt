from typing import Dict


class DomainSerializer:
    def from_json(self, data: Dict[str, str]):
        raise NotImplemented

    def to_json(self, domain_object) -> Dict[str, str]:
        res = {}
        for name, value in domain_object.__dict__.items():
            if not name.startswith('_'):
                res[name] = value
        return res

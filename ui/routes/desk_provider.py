from flask import jsonify, request
from application.desks.desk import Desk
from abc import ABC, abstractmethod
from typing import Dict


class DeskProvider(ABC):
    def __init__(self, desk: Desk):
        self.desk = desk

    def jsonify_n_serialized_objects_from_desk(self, name: str):
        page_number = int(request.args.get('page_number'))
        items, page_count = self.desk.get(page_number)
        ans_dict = {
            "count": page_count,
            name: [
                self.domain_to_json(item) for item in items
            ]
        }

        return jsonify(ans_dict)

    @abstractmethod
    def get(self):
        pass

    @staticmethod
    def domain_to_json(obj) -> Dict[str, str]:
        res = {}
        for name, value in obj.__dict__.items():
            if not name.startswith('_'):
                res[name] = value
        return res

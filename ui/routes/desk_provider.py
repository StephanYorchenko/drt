from flask import jsonify, request
from application.desks.desk import Provider
from abc import ABC, abstractmethod
from typing import Dict


class DeskProvider:
    def __init__(self, desk: Provider, name=''):
        self.desk = desk
        self._name = name

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

    def get(self):
        return self.jsonify_n_serialized_objects_from_desk(
            self._name
        )

    @staticmethod
    def domain_to_json(obj) -> Dict[str, str]:
        res = {}
        for name, value in obj.__dict__.items():
            if not name.startswith('_'):
                res[name] = value
        return res

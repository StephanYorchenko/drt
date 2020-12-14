from flask import jsonify, request
from application.providers.provider import Provider
from typing import Dict


class Desk:
    def __init__(self, provider: Provider, transformer, name=''):
        self.provider = provider
        self._name = name
        self.transformer = transformer

    def jsonify_n_serialized_objects_from_desk(self, name: str):
        page_number = int(request.args.get('page_number'))
        items, page_count = self.provider.get(page_number)
        ans_dict = {
            "count": page_count,
            name: [
                self.transformer.to_json(item) for item in items
            ]
        }

        return jsonify(ans_dict)

    def get(self):
        return self.jsonify_n_serialized_objects_from_desk(
            self._name
        )

    def add(self):
        data = request.form
        json = dict(
            title=data.get('title'),
            text=data.get('text'),
            username=data.get('username')
        )
        self.provider.add(self.transformer.from_json(json))

    @staticmethod
    def domain_to_json(obj) -> Dict[str, str]:
        res = {}
        for name, value in obj.__dict__.items():
            if not name.startswith('_'):
                res[name] = value
        return res

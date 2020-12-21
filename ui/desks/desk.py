from flask import jsonify, request, abort
from application.providers.provider import Provider
from typing import Dict


def permission_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PermissionError:
            abort(403)
    return wrapper


class Desk:
    def __init__(self, provider: Provider, transformer, name=''):
        self.provider = provider
        self._name = name
        self.transformer = transformer

    def get_caller_name(self):
        return request.cookies.get('name')

    def get_n_jsonified_objects(self, name: str):
        page_number = int(request.args.get('page_number'))
        items, page_count = self.provider.get(page_number,
                                              self.get_caller_name())
        ans_dict = {
            "count": page_count,
            name: [
                self.transformer.to_json(item) for item in items
            ]
        }

        return jsonify(ans_dict)

    def get_all_jsonified_objects(self, name):
        ans_dict = {
            'count': 1,
            name: list(
                map(
                    self.transformer.to_json,
                    self.provider.get_all(self.get_caller_name())
                )
            )
        }
        return jsonify(ans_dict)

    @permission_error_handler
    def get(self):
        if 'page_number' not in request.args:
            return self.get_all_jsonified_objects(self._name)
        return self.get_n_jsonified_objects(self._name)

    @permission_error_handler
    def add(self):
        return self.provider.add(self.transformer.from_json(
            self.get_json(request.form)), self.get_caller_name())

    @staticmethod
    def get_json(data):
        json = dict()
        for key in list(data.keys()):
            json[key] = data[key]
        return json

    @staticmethod
    def domain_to_json(obj) -> Dict[str, str]:
        res = {}
        for name, value in obj.__dict__.items():
            if not name.startswith('_'):
                res[name] = value
        return res

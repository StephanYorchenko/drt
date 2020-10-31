from domain.desk import Desk
from flask import request, jsonify


def jsonify_n_serialized_objects_from_desk(desk: Desk, name: str):
    page_number = request.args.get('page')
    items = desk.get(page_number)
    ans_dict = {
        "count": len(items),
        name: [
            item.to_json() for item in items
        ]
    }

    return jsonify(ans_dict)

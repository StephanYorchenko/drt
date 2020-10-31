from domain.desk import Desk
from flask import request, jsonify


def jsonify_n_serialized_objects_from_desk(desk: Desk, name: str):
    page_number = request.args.get('page')
    items, page_count = desk.get(page_number)
    ans_dict = {
        "count": page_count,
        name: [
            item.to_json() for item in items    
        ]
    }

    return jsonify(ans_dict)

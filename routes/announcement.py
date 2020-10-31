from flask import request, jsonify
from domain.desk.desk import Desk


def get_announcements():
    page_number = request.args.get('page')
    announcements = Desk.get_announcements(page_number)
    ans_dict = {
        "count": len(announcements),
        "announcements": [
            announcement.to_json() for announcement in announcements
        ]
    }

    return jsonify(ans_dict)

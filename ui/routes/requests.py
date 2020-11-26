from .get_items_from_desk import jsonify_n_serialized_objects_from_desk
from application.desks.request_desk import RequestDesk


def get_announcements():
    return jsonify_n_serialized_objects_from_desk(RequestDesk(),  'requests')

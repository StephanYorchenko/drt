from .get_items_from_desk import jsonify_n_serialized_objects_from_desk
from domain.desk.desk import Desk


def get_announcements():
    return jsonify_n_serialized_objects_from_desk(Desk,  'requests')

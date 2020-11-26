from .get_items_from_desk import jsonify_n_serialized_objects_from_desk
from application.desks.announcement_desk import AnnouncementDesk


def get_announcements():
    return jsonify_n_serialized_objects_from_desk(AnnouncementDesk,  'requests')

from domain.desk.announcement_desk import AnnouncementDesk
from .get_items_from_desk import jsonify_n_serialized_objects_from_desk


def get_announcements():
    return jsonify_n_serialized_objects_from_desk(AnnouncementDesk,
                                                  'announcements')

from application.desks.announcement_desk import AnnouncementDesk
from .desk_provider import DeskProvider


class AnnouncementProvider(DeskProvider):
    def __init__(self):
        super().__init__(AnnouncementDesk())

    def get(self):
        return self.jsonify_n_serialized_objects_from_desk(
            'announcements'
        )

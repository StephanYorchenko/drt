from ui.desks import Desk
from application import AnnouncementProvider


class AnnouncementDesk(Desk):
    def __init__(self, provider: AnnouncementProvider, name: str):
        super().__init__(provider, name)

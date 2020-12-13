from ui.desks.desk import Desk
from ui.transformers import AnnouncementJsonTransformer
from application import AnnouncementProvider


class AnnouncementDesk(Desk):
    def __init__(self, provider: AnnouncementProvider,
                 transformer: AnnouncementJsonTransformer, name: str):
        super().__init__(provider, transformer, name)

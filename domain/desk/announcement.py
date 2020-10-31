from domain.Serializable import Serializable


class Announcement(Serializable):
    def __init__(self, ann_id: int, topic: str, text: str):
        self.id = ann_id
        self.topic = topic
        self.text = text

from Domain.Serializable import Serializable


class Announcement(Serializable):
    def __init__(self, ann_id: int, topic: str, text: str, user_id: int):
        self.id = ann_id
        self.topic = topic
        self.text = text
        self.user_id = user_id

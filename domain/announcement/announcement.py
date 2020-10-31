import typing

from domain.serializable import Serializable


class Announcement(Serializable):
    def __init__(self, title: str, text: str, user_id: int):
        self.topic = title
        self.text = text
        self.user_id = user_id

    @staticmethod
    def from_json(data: typing.Dict[str, str]):
        return Announcement(data['title'], data['text'], int(data['id']))

from typing import Dict
from .domain_serializer import DomainSerializer
from domain.announcement.announcement import Announcement


def from_json(data: Dict[str, str]) -> Announcement:
    return Announcement(data['title'], data['text'], int(data['id']),
                        data['date'])


class AnnouncementSerializer(DomainSerializer):
    def __init__(self):
        super().__init__(from_json)

from typing import Dict
from .domain_serializer import DomainSerializer
from domain.announcement.announcement import Announcement


class AnnouncementSerializer(DomainSerializer):
    def from_json(self, data: Dict[str, str]) -> Announcement:
        return Announcement(data['title'], data['text'], int(data['id']),
                            data['date'])

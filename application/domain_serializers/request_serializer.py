from typing import Dict
from .domain_serializer import DomainSerializer
from domain.request.request import Request
from domain.request.requestType import HostessRequestType


class RequestSerializer(DomainSerializer):
    def to_json(self, request: Request) -> Dict[str, str]:
        # noinspection PyProtectedMember
        return {'id': request._id, 'request_type': request._type,
                'comment': request._comment, 'user_id': request._user}

    def from_json(self, data: Dict[str, str]) -> Request:
        return Request(int(data['id']),
                       HostessRequestType(data['request_type']),
                       data['comment'],
                       int(data['user_id']))

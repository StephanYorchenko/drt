from typing import Dict
from .domain_serializer import DomainSerializer
from domain.request.request import Request
from domain.request.requestType import HostessRequestType


def from_json(data: Dict[str, str]) -> Request:
    return Request(int(data['id']),
                   HostessRequestType(data['request_type']),
                   data['comment'],
                   int(data['user_id']))


class RequestSerializer(DomainSerializer):
    def __init__(self):
        super().__init__(from_json)

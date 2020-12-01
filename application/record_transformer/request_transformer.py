from typing import Dict
from .domain_transformer import DomainTransformer
from domain.request.request import Request
from domain.request.requestType import HostessRequestType


class RequestTransformer(DomainTransformer):
    def __init__(self):
        super().__init__(lambda record:
                         Request(record.id, HostessRequestType(record.topic),
                                 record.comment, record.user_id,
                                 record.is_watched))

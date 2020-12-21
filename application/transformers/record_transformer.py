from typing import Dict
from application.transformers.announcement_record \
    import AnnouncementRecordTransformer
from application.transformers.request_record \
    import RequestRecordTransformer
from application.transformers.user_record import \
    UserRecordTransformer
from application.transformers.table_request_record import \
    TableRequestRecordTransformer


class RecordTransformer(AnnouncementRecordTransformer,
                        RequestRecordTransformer,
                        UserRecordTransformer,
                        TableRequestRecordTransformer):
    def __init__(self, from_record, to_record):
        self.from_record = from_record
        self.to_record = to_record

from typing import Dict
from application.transformers.announcement_record_transformer \
    import AnnouncementRecordTransformer
from application.transformers.request_record_transformer \
    import RequestRecordTransformer
from application.transformers.user_record_transformer import \
    UserRecordTransformer


class RecordTransformer(AnnouncementRecordTransformer,
                        RequestRecordTransformer,
                        UserRecordTransformer):
    def __init__(self, from_record, to_record):
        self.from_record = from_record
        self.to_record = to_record

from __future__ import annotations
from typing import Dict


class Announcement:
    def __init__(self, title: str, text: str, user_id: int, date: str):
        self.title = title
        self.text = text
        self.user_id = user_id
        self.date = date

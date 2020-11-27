from dataclasses import dataclass

from typing import Dict


@dataclass
class Announcement:
    title: str
    text: str
    user_id: int
    date: str

from dataclasses import dataclass


@dataclass
class Announcement:
    title: str
    text: str
    user_id: int
    date: str

from dataclasses import dataclass


@dataclass
class Announcement:
    title: str
    text: str
    date: str

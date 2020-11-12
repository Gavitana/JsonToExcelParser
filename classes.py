from dataclasses import dataclass


@dataclass
class Card:
    id: str
    creator: str
    labels: str
    title: str
    hours: int = 0

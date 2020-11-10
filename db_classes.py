from dataclasses import dataclass


@dataclass
class Card:
    id: str
    title: str
    creator: str
    labels: str = "-"

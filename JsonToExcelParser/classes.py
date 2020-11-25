from dataclasses import dataclass


@dataclass
class Card:
    id: str
    creator: str = "Никто не назначен"
    labels: str = ""
    title: str = ""
    hours: int = 0

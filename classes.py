from dataclasses import dataclass


@dataclass
class Card:
    id: str
    title: str
    creator: str
    labels: str = "-"
    hours: int = 0

@dataclass
class Result:
    name: str
    hours: int = 0

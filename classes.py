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
    project: str
    hours: int = 0


@dataclass
class Creator:
    creator: str = '-'
    creator_hours: int = 0

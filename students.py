students = [
    {"name": "John", "score": 85},
    {"name": "Mary", "score": 91},
    {"name": "David", "score": 74}
]

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    score: int
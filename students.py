"""students.py - Student data module.

Holds the list of students and the Student data model
used across the application.
"""

from dataclasses import dataclass


@dataclass
class Student:
    """Represents a single student record."""
    name: str
    score: int


# Raw student records (dictionary form, used by helpers.py)
students = [
    {"name": "John", "score": 85},
    {"name": "Mary", "score": 91},
    {"name": "David", "score": 74},
]


def get_students():
    """Return the list of student records."""
    return students


def add_student(name, score):
    """Add a new student to the records.

    Args:
        name (str): Student's name.
        score (int): Student's score.
    """
    students.append({"name": name, "score": score})
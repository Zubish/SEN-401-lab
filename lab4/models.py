"""models.py - Data models for Lab 4 refactor."""

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: int


@dataclass
class InventoryItem:
    item_name: str
    quantity: int
    price: int
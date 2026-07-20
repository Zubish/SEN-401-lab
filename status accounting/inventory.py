"""inventory.py - Inventory data module for Lab 3 (Status Accounting)."""

inventory = [
    {"item_name": "Pen", "quantity": 50, "price": 100},
    {"item_name": "Notebook", "quantity": 30, "price": 250},
    {"item_name": "Marker", "quantity": 20, "price": 150},
]

from dataclasses import dataclass

@dataclass
class InventoryItem:
    item_name: str
    quantity: int
    price: int

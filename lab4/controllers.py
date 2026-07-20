"""controllers.py - Business logic tying models and utils together."""

from utils import average, highest, lowest

students = [
    {"name": "John", "score": 85},
    {"name": "Mary", "score": 91},
    {"name": "David", "score": 74},
]

inventory = [
    {"item_name": "Pen", "quantity": 50, "price": 100},
    {"item_name": "Notebook", "quantity": 30, "price": 250},
    {"item_name": "Marker", "quantity": 20, "price": 150},
]


def student_report():
    scores = [s["score"] for s in students]
    return {
        "average": average(scores),
        "highest": highest(students, key=lambda s: s["score"]),
        "lowest": lowest(students, key=lambda s: s["score"]),
    }


def inventory_report():
    return {
        "total_value": sum(i["quantity"] * i["price"] for i in inventory),
        "highest_stock": highest(inventory, key=lambda i: i["quantity"]),
        "lowest_stock": lowest(inventory, key=lambda i: i["quantity"]),
    }


if __name__ == "__main__":
    print("Student Report:", student_report())
    print("Inventory Report:", inventory_report())
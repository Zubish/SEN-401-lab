"""app.py - Demo app for Lab 3 (Status Accounting)."""

from inventory import inventory
from helpers import total_stock_value, highest_stock_item, lowest_stock_item

print("Inventory Report")
for item in inventory:
    print(f"{item['item_name']:<10}{item['quantity']:>6}{item['price']:>8}")

print(f"\nTotal Stock Value: {total_stock_value(inventory)}")
print(f"Highest Stock: {highest_stock_item(inventory)['item_name']}")

print(f"Lowest Stock : {lowest_stock_item(inventory)['item_name']}")

print(f"Lowest Stock : {lowest_stock_item(inventory)['item_name']}")

def average_price(items):
    if len(items) == 0:
        return 0
    return sum(i["price"] for i in items) / len(items)


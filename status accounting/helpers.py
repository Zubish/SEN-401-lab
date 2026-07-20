"""helpers.py - Helper functions for inventory calculations."""

def total_stock_value(items):
    """Return total value of all inventory items."""
    if len(items) == 0:
        return 0
    return sum(i["quantity"] * i["price"] for i in items)


def highest_stock_item(items):
    """Return the item with the highest quantity."""
    if len(items) == 0:
        return None
    return max(items, key=lambda i: i["quantity"])


def lowest_stock_item(items):
    """Return the item with the lowest quantity."""
    if len(items) == 0:
        return None

    return min(items, key=lambda i: i["quantity"])

    return min(items, key=lambda i: i["quantity"])

def total_stock_value(items):
    if len(items) == 0:
        return 0
    return sum(i["quantity"] * i["price"] for i in items)


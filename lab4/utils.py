"""utils.py - Shared calculation helpers for Lab 4."""

def average(values):
    """Return the average of a list of numbers, or 0 if empty."""
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


def highest(items, key):
    """Return the item with the highest value for the given key."""
    if len(items) == 0:
        return None
    return max(items, key=key)


def lowest(items, key):
    """Return the item with the lowest value for the given key."""
    if len(items) == 0:
        return None
    return min(items, key=key)
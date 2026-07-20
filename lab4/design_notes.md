# Design Notes - Reverse Engineering (Lab 4)

## Existing Modules
- students.py: student list (name, score), Student dataclass
- utils/helpers.py: highest_score(), lowest_score(), average_score()
- status accounting/inventory.py: inventory list, InventoryItem dataclass
- status accounting/helpers.py: total_stock_value(), highest_stock_item(), lowest_stock_item()
- app.py files: import data + helpers, print reports

## Dependencies
- app.py depends on students.py/inventory.py (data) and helpers.py (logic)
- No circular dependencies found

## Code Smells / Coupling Issues
- Data and print logic mixed directly in app.py (low separation of concerns)
- Duplicate helper function patterns across student and inventory modules
- No shared base module for common calculations (e.g. average logic repeated)
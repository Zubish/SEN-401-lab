"""database.py - SQLite migration for Lab 4."""

import sqlite3

def init_db():
    conn = sqlite3.connect("lab4.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price INTEGER NOT NULL
        )
    """)

    students = [("John", 85), ("Mary", 91), ("David", 74)]
    cur.executemany("INSERT INTO students (name, score) VALUES (?, ?)", students)

    inventory = [("Pen", 50, 100), ("Notebook", 30, 250), ("Marker", 20, 150)]
    cur.executemany("INSERT INTO inventory (item_name, quantity, price) VALUES (?, ?, ?)", inventory)

    conn.commit()
    conn.close()
    print("Database initialized: lab4.db created with sample data.")

if __name__ == "__main__":
    init_db()
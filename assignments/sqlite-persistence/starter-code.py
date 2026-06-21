"""
Persistent Python APIs with SQLite
=================================

This starter code shows how to create a SQLite-backed application using Python.
Students should complete the database CRUD functions and connect them to a simple
interface.
"""

import sqlite3
from sqlite3 import Connection
from typing import List, Optional, Tuple

DB_PATH = "items.db"


class Item:
    def __init__(self, item_id: int, name: str, description: str, price: float):
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Item(id={self.id}, name={self.name}, description={self.description}, price={self.price})"


# ============================================================================
# Database Helpers
# ============================================================================

def create_connection(db_path: str) -> Connection:
    """Create a database connection to the SQLite database."""
    connection = sqlite3.connect(db_path)
    return connection


def create_table(connection: Connection) -> None:
    """Create the items table if it does not exist."""
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL
        )
        """
    )
    connection.commit()


def insert_item(connection: Connection, name: str, description: str, price: float) -> int:
    """Insert a new item and return its ID."""
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
        (name, description, price),
    )
    connection.commit()
    return cursor.lastrowid


def get_all_items(connection: Connection) -> List[Item]:
    """Return all items from the database."""
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, description, price FROM items")
    rows = cursor.fetchall()
    return [Item(item_id=row[0], name=row[1], description=row[2], price=row[3]) for row in rows]


def get_item_by_id(connection: Connection, item_id: int) -> Optional[Item]:
    """Return a single item by ID."""
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, name, description, price FROM items WHERE id = ?",
        (item_id,),
    )
    row = cursor.fetchone()
    if row:
        return Item(item_id=row[0], name=row[1], description=row[2], price=row[3])
    return None


def update_item(connection: Connection, item_id: int, name: str, description: str, price: float) -> bool:
    """Update an existing item. Return True if updated."""
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?",
        (name, description, price, item_id),
    )
    connection.commit()
    return cursor.rowcount > 0


def delete_item(connection: Connection, item_id: int) -> bool:
    """Delete an item by ID. Return True if deleted."""
    cursor = connection.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    connection.commit()
    return cursor.rowcount > 0


# ============================================================================
# User Interface
# ============================================================================

def print_menu() -> None:
    print("\nSQLite Item Manager")
    print("1. View all items")
    print("2. Add a new item")
    print("3. Update an item")
    print("4. Delete an item")
    print("5. Exit")


def prompt_for_item_data() -> Tuple[str, str, float]:
    name = input("Item name: ")
    description = input("Item description: ")
    price = float(input("Item price: "))
    return name, description, price


def main() -> None:
    connection = create_connection(DB_PATH)
    create_table(connection)

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            items = get_all_items(connection)
            if not items:
                print("No items found.")
            else:
                for item in items:
                    print(item)

        elif choice == "2":
            name, description, price = prompt_for_item_data()
            item_id = insert_item(connection, name, description, price)
            print(f"Added item with ID {item_id}.")

        elif choice == "3":
            item_id = int(input("Item ID to update: "))
            existing = get_item_by_id(connection, item_id)
            if not existing:
                print("Item not found.")
                continue
            print(f"Updating: {existing}")
            name, description, price = prompt_for_item_data()
            if update_item(connection, item_id, name, description, price):
                print("Item updated successfully.")
            else:
                print("Update failed.")

        elif choice == "4":
            item_id = int(input("Item ID to delete: "))
            if delete_item(connection, item_id):
                print("Item deleted.")
            else:
                print("Item not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")

    connection.close()


if __name__ == "__main__":
    main()

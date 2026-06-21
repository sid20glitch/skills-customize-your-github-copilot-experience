# 📘 Assignment: Persistent Python APIs with SQLite

## 🎯 Objective

Build a Python application that stores and retrieves data using SQLite. Students will learn how to use database persistence to make applications that keep data across runs, using Python’s standard library and simple SQL queries.

## 📝 Tasks

### 🛠️ Set Up a SQLite Database

#### Description
Create a SQLite database file and define a table schema for storing records. Use Python’s built-in `sqlite3` module to connect to the database and create the table if it does not already exist.

#### Requirements
Completed program should:

- Create or open a SQLite database file
- Define a table schema for the chosen data model
- Use `sqlite3.connect()` to connect to the database
- Create the table on startup if it does not exist
- Close the database connection cleanly

### 🛠️ Implement CRUD Operations

#### Description
Write functions to create, read, update, and delete records in the SQLite database. The application should use SQL queries and parameterized statements to safely manage stored data.

#### Requirements
Completed program should:

- Insert new records into the database
- Read all records and display them to the user
- Update a record by ID
- Delete a record by ID
- Use parameterized SQL queries to avoid SQL injection

### 🛠️ Connect the Database to an API Interface

#### Description
Build a simple API interface or command-line flow around the database functions so users can interact with stored records. Demonstrate database persistence by saving data, exiting, and restarting the app.

#### Requirements
Completed program should:

- Provide a simple interface for interacting with stored records
- Use the SQLite-backed CRUD functions within the interface
- Show that inserted records remain available across separate runs
- Handle invalid record IDs with clear messages
- Use meaningful output for each operation

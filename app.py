import sqlite3

# connecting to the database / creating one if it does not exist
db = './tasks.db'
conn = sqlite3.connect(db)
cursor = conn.cursor

# creating a table in the database (this only happens on first run)
query = """CREATE TABLE tasks
(TaskID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Title TEXT NOT NULL,
Details TEXT NOT NULL,
Dateadded TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
Removed BOOLEAN NOT NULL DEFAULT FALSE
)
"""

cursor.execute(query)
conn.commit()

def main():
    print("\nPlease select from the following options:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")  
    print("4. View all removed tasks")
    print("5. Permenantly delete a task")    
    print("6. View a specific task")
    print("7. Update a task")
    print("8. Exit")

    user_choice = input("Please enter your choice: ")

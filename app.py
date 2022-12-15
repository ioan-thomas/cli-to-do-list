import sqlite3

# connecting to the database / creating one if it does not exist
db = './tasks.db'
conn = sqlite3.connect(db)
cursor = conn.cursor()

def createTable(table_name):
    # this function creates a table in the database if it doesn't already exist

    # the SQL query to be run 
    query = f"""CREATE TABLE ?
    (TaskID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Title TEXT NOT NULL,
    Details TEXT NOT NULL,
    Dateadded TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Removed BOOLEAN NOT NULL DEFAULT FALSE)"""

    # attempts to create the table using the above query but shows a message if one already exists
    try: 
        cursor.execute(query, (table_name,))
        conn.commit()
    except sqlite3.OperationalError:
        print("Database table already exists.")


def addTask():
    # this function adds a task to the database.

    # prompts user for input.
    Title = str(input("Please enter a title: "))

    # if the user does not enter an input, a default message is added to the variable
    Details = str(input("Please enter details for the task or click Enter to skip: ")) or "There are no details for this task."

    # query is formed based on the values given by the user.
    query = """INSERT INTO tasks (Title, Details) VALUES (?, ?)
    """

    # attempts to add the task information to the database.
    try: 
        cursor.execute(query, (Title, Details))

    # throws an error if adding the task to the database was unsuccessful for any reason. 
    except:
        print("There was an error adding the task. Please try again.")

    # saves the changes to the databse and prints a success message.
    else: 
        conn.commit()
        print(f"The task '{Title}' was added successfully.")


def main():
    # presents the user with options, asks user for input and runs the relevant function associated with that output.

    while True:
        print("\nPlease select from the following options:")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Remove a task")  
        print("4. View all removed tasks")
        print("5. Permenantly delete a task")    
        print("6. View a specific task")
        print("7. Update a task")
        print("8. Exit")
        
        # promts user for decision
        user_choice = input("Please enter your choice: ")

        # runs the relevant function associated with the user's output and then breaks out of the loop.
        if user_choice == "1":
            addTask()
            return
        if user_choice == "2":
            print("2")
            return
        if user_choice == "3":
            print("3")
            return
        if user_choice == "4":
            print("4")
            return
        if user_choice == "5":
            print("5")
            return
        if user_choice == "6":
            print("6")
            return
        if user_choice == "7":
            print("7")
            return
        if user_choice == "8":
            print("8")
            return


if __name__ == "__main__":

    createTable('tasks')

    # runs the 'main function' i.e. the main menu
    main()

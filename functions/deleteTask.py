from functions.viewTasks import viewTasks

def deleteTask(conn, cursor):
    # this function permanently deletes tasks from the tasks database

    while True:
        # the user is shown all of the tasks available
        viewTasks(conn, cursor, False)

        #the user is promted to enter the ID of the task they would like to delete
        taskID = str(input("Enter the ID of the task you wish to permanently delete: "))

        # the SQL query to be ran. It deleted the task with the given taskID from the tasks database.
        query = """DELETE FROM tasks WHERE taskID = ?"""

        # attempts to execute the query with the given taskID using parameterisation.
        try: 
            cursor.execute(query, (taskID,))
        except:
            # displays the message if an error has occurred.
            print("There was an error deleting that task. Please try again.")
        else: 
            # saves the changes to the database and displays the message.
            conn.commit()
            print(f"The task with the ID of {taskID} has been deleted.")

            # prompts the user for an input.
            userInput = str(input("Would you like to delete another task? (Y/N): ")).upper()
            # if the user selects they would not like to delete another task, they are returned to the main menu. Otherwise, the loop continues and they are shown a list of tasks again to delete.
            if userInput == 'N':
                return


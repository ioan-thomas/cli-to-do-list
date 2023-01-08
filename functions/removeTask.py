from functions.viewTasks import viewTasks
from functions.exitApp import exitApp

def removeTask(conn, cursor):
    # this function removes the specified task from the to-do-list, but does not remove it from the database.


    while True:
        try:
            # asks user for ID, if user enters "TASKS" (or anything else other than an ID) a valueError will be thrown (see below).
            taskID = int(input("Enter the ID of the task that you wish to remove or type TASKS to list all tasks: "))

            # the SQL query to be ran. The Removed value associated with the given taskID (in the tasks table) is set to True.
            query = """UPDATE tasks SET Removed = TRUE WHERE TaskID = ?"""
            
            #executing the SQL query above with the task as the parameter (in place of the "?").
            cursor.execute(query, (taskID,))

        # if the user input results in anything other than an integer (a taskID), then the user will be shown the list of tasks
        except ValueError:
            # imported from functions/viewTasks.py
            viewingTasks = viewTasks(conn, cursor, False)
            if viewingTasks == -1:
                return
        # if user exits app, they are greeted with the goodbye message throught the exitApp function
        except KeyboardInterrupt:
            exitApp() # imported from functions/exitApp.py

        # if an error occurs, the user will be presented with the below error text.
        except:
            print('There was an error removing that task. Please check the taskID and try again.')

        # commits the changes to the tasks database and presents the user with the message.
        else:
            conn.commit()
            print(f"If there is task with the ID of {taskID}, it has been removed.")
            
            # asks the user if they want to remove another task. If they do, they are returned to the main menu
            userChoice = str(input("Would you like to remove another task? (Y/N): ")).upper()
            if userChoice == 'N':
                return


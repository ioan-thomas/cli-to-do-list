from functions.viewTasks import viewTasks
from functions.exitApp import exitApp

def deleteTask(conn, cursor):
    # this function permanently deletes tasks from the tasks database

    while True:
        try: 
            # the user is shown all of the tasks available
            viewing_tasks = viewTasks(conn, cursor, False, False)
            if viewing_tasks == -1:
                return
                
            #the user is promted to enter the ID of the task they would like to delete
            task_ID = str(input("Enter the ID of the task you wish to permanently delete: "))

            # the SQL query to be ran. It deleted the task with the given taskID from the tasks database.
            query = """DELETE FROM tasks WHERE taskID = ?"""

            # attempts to execute the query with the given taskID using parameterisation.
 
            cursor.execute(query, (task_ID,))
        
         #exits the app on keyboard interrupt
        except KeyboardInterrupt:
            exitApp()

        except:
            # displays the message if an error has occurred.
            print("An error occurred. Please try again.")
            return
        else: 
            # saves the changes to the database and displays the message.
            conn.commit()
            print(f"The task with the ID of {task_ID} has been deleted.")

            # prompts the user for an input.
            user_input = str(input("Would you like to delete another task? (Y/N): ")).upper()
            # if the user selects they would not like to delete another task, they are returned to the main menu. Otherwise, the loop continues and they are shown a list of tasks again to delete.
            if user_input == 'N':
                return


from functions.viewTasks import viewTasks
from functions.exitApp import exitApp

def updateTask(conn, cursor):

    # this function allows the user to update an task information
    while True:
        # displays a list of tasks to the user
        viewingTasks = viewTasks(conn, cursor, False, False)

        # if there are no tasks available, the user will be returned to the main menu
        if viewingTasks == -1: 
            return
        try: 
            # prompts user for the task details
            taskID = int(input("Enter the task ID you wish to update: "))
            taskTitle = str(input("Enter the title of the task: ")).capitalize()
            
            # checks if the title is less than 100 characters
            if len(taskTitle) > 100:
                print("The title must be less than 100 characters.")
                continue

            taskDetails = str(input("Please enter details for the task or click Enter to skip: ")) or "There are no details for this task."

            # checks if the details are less than 250 characters
            if len(taskDetails) > 250:
                print("The details must be less than 250 characters.")
                continue

            # the SQL query to be ran
            query = """UPDATE tasks SET Title = ?, Details = ? WHERE TaskID = ?"""

            # executes the query
            cursor.execute(query, (taskTitle, taskDetails, taskID))
        
        # if the user attempts to exit the app, the below exitApp function is ran.
        except KeyboardInterrupt:
                exitApp()
        except:
            # catches any unexpected error and prints the below message.
            print("Invalid input. Please check the task ID and try again.")
            continue
        else:
            # commits the changes to the database and prints a message saying so.
            conn.commit()
            print(f"The task with the ID {taskID} has been updated.")
            
            # asks user if they would like to update another task.
            userChoiceToExit = str(input("Do you wish to update another task? (Y/N): ")).upper()

            # if user chooses to exit, they are returned to the main menu.
            if userChoiceToExit == 'N':
                return

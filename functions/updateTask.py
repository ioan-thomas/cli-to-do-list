from functions.viewTasks import viewTasks
from functions.exitApp import exitApp

def updateTask(conn, cursor):

    # change way that viewTasks works - check for value in parameters, if there display the option for viewing more details
    while True:
        viewTasks(conn, cursor, False)

        try: 
            taskID = int(input("Enter the task ID you wish to update: "))
            taskTitle = str(input("Enter the title of the task: "))
            taskDetails = str(input("Enter the details for the task: "))

            query = """UPDATE tasks SET Title = ?, Details = ? WHERE TaskID = ?"""

            cursor.execute(query, (taskTitle, taskDetails, taskID))
        
        except KeyboardInterrupt:
                exitApp()
        except:
            print("Invalid input. Please check the task ID and try again.")
        else:
            conn.commit()
            print(f"The task with the ID {taskID} has been updated.")
            
            userChoiceToExit = str(input("Do you wish to update another task? (Y/N): ")).upper()

            if userChoiceToExit == 'N':
                return

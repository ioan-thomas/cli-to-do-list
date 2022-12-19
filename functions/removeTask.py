from functions.viewTasks import viewTasks

def removeTask(conn, cursor):
    # this function removes the specified task from the to-do-list, but does not remove it from the database.

    while True:
        try:
            # asks user for ID, or 
            taskID = input("Enter the ID of the task that you wish to remove or type TASKS to list all tasks: ")
            query = """UPDATE tasks SET Removed = TRUE WHERE TaskID = ?"""

            if type(taskID) != "<class 'str'>":
                cursor.execute(query, (int(taskID),))

        except:
            print('There was an error removing that task. Please check the taskID and try again.')

        else:
            
            if type(taskID) == "<class 'str'>":
                viewTasks(conn, cursor)
            else:
                conn.commit()
                print(f"The task with the ID {taskID} has been removed")
                return


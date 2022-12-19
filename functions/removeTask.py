from functions.viewTasks import viewTasks

def removeTask(conn, cursor):
    # this function removes the specified task from the to-do-list, but does not remove it from the database.

    while True:
        try:
            # asks user for ID, or 
            taskID = int(input("Enter the ID of the task that you wish to remove or type TASKS to list all tasks: "))
            query = """UPDATE tasks SET Removed = TRUE WHERE TaskID = ?"""
            
            cursor.execute(query, (taskID,))

        except ValueError:
            viewTasks(conn, cursor)
        except:
            print('There was an error removing that task. Please check the taskID and try again.')

        else:
            conn.commit()
            print(f"If there is task with the ID {taskID}, it has been removed")
            return


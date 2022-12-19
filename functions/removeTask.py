def removeTask(conn, cursor):
    # this function removes the specified task from the database, but does not removed it.

    while True:
        try:
            taskID = int(input("Enter the ID of the task that you wish to remove: "))
            query = """UPDATE tasks SET Removed = TRUE WHERE TaskID = ?"""
            cursor.execute(query, (taskID,))
            
        except:
            print('There was an error removing that task. Please check the taskID and try again.')
        else:
            conn.commit()
            print(f"The task with the ID {taskID} has been removed")
            return


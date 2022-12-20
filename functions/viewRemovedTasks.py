def viewRemovedTasks(conn, cursor):
    # this function allows the user to view all tasks from the database that have been marked as removed.

    query = """SELECT * FROM tasks WHERE Removed = 1"""

    cursor.execute(query)
    results = cursor.fetchall()

    print("Here are all the tasks that have been marked as removed: \n")

    if results == []:
        print("There are no tasks that have been removed.")
    
    else: 
        for task in results:
            for item in task:
                print(item, end=" ")
            print("\n")

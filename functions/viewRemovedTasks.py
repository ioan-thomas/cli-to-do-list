def viewRemovedTasks(conn, cursor):
    # this function allows the user to view all tasks from the database that have been marked as removed.

    # this is the SQL function to be ran. All values from the tasks table are selected if under the Removed column there is a 1 (True).
    query = """SELECT * FROM tasks WHERE Removed = 1"""

    #executes the above query using the cursor object.
    cursor.execute(query)

    # fetches all of the results relating to the above query into a list.
    results = cursor.fetchall()

    print("Here are all the tasks that have been marked as removed: \n")

    # if the list contains no values, the below message will be shown to the user in the console.
    if results == []:
        print("There are no tasks that have been removed.")
    
    # loops through the array of results returned from the database and prints them to the console.
    else: 
        for task in results:
            for item in task:
                print(item, end=" ")
            print("\n")

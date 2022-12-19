from functions.viewAllDetails import viewAllDetails

def viewTasks(conn, cursor):
    # this function retrieves all tasks from the database that have not been removed

    # querying the database for the relevant information
    query = """SELECT TaskID, Title, Details, Dateadded FROM tasks WHERE Removed = 0"""
    cursor.execute(query)

    # fetching all of the results from the database
    results = cursor.fetchall()

    # WHAT IF THERE'S NOT ANY???

    # printing results to the terminal 
    print("Here are all the tasks:\n")
    for task in results:
        print(f"""\n{task[0]}: {task[1]}\n""")

    while True:
        print("Would you like to view all task details? (Y/N)")
        user_choice = str(input()).upper()

        if user_choice == 'Y':
            viewAllDetails(results)
            return
        if user_choice == 'N':
            return

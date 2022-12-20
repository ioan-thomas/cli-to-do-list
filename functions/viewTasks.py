from functions.viewAllDetails import viewAllDetails

def viewTasks(conn, cursor, viewDetails):
    # this function retrieves all tasks from the database that have not been removed

    # querying the database for the relevant information
    query = """SELECT TaskID, Title, Details, Dateadded FROM tasks WHERE Removed = 0"""
    cursor.execute(query)

    # fetching all of the results from the database into a list.
    results = cursor.fetchall()

    # if the list is empty, the below message is shown in the console and the user is returned to main function that called this viewTasks function.
    if results == []:
        print("\n There aren't any tasks yet.")
        return

    # printing results to the terminal 
    print("Here are all the tasks:\n")
    for task in results: 
        print(f"""\n{task[0]}: {task[1]}\n""")


    # the viewDetails parameter allows for added functionality within this function. If the user should be given the option to view more details about the task then the below code is ran.
    # the user is prompted whether or not they would like to view more details. If the user selects yes then the viewAllDetails function is ran displaying those details. If not, the user is returned to the main() function which is where this viewTasks function was called.
    if viewDetails:
        while True:
            user_choice = str(input("Would you like to view all task details? (Y/N): ")).upper()

            if user_choice == 'N':
                return
            
            viewAllDetails(results)

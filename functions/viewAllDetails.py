def viewAllDetails(tasks): 
    # this function loops through the list given as an argument (tasks) and outputs the values to the console.
    try:
        for task in tasks:
            print(f"""\n
            {task[0]}: {task[1]}\n
            Details: {task[2]}\n
            Time created: {task[3]}\n
            """)
    # catches any errors that occur during the process e.g. the array is somehow empty.
    except:
        print("An error occurred. Please try again.\n")

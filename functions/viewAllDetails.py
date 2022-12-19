def viewAllDetails(tasks): 
    try:
        for task in tasks:
            print(f"""\n
            {task[0]}: {task[1]}\n
            Details: {task[2]}\n
            Time created: {task[3]}\n
            """)
    except:
        print("An error occurred. Please try again.\n")

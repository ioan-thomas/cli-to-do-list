from functions.exitApp import exitApp

def addTask(conn, cursor):
    # this function adds a task to the database.
    try: 

        # prompts user for input. Capitalises the input creating for a better UX (increased readability) when viewing the tasks later.
        Title = str(input("Please enter a title: ")).capitalize()

        # if the user does not enter an input, a default message is added to the variable
        Details = str(input("Please enter details for the task or click Enter to skip: ")) or "There are no details for this task."

        # query is formed based on the values given by the user using parameterisation. The query will insert the parameter values into values table under the Title and Details columns respectively.
        query = """INSERT INTO tasks (Title, Details) VALUES (?, ?)
        """

    # attempts to add the task information to the database.
    
        cursor.execute(query, (Title, Details))
    
    #exits the app on keyboard interrupt
    except KeyboardInterrupt:
        exitApp()

    # throws an error if adding the task to the database was unsuccessful for any reason. 
    except:
        print("There was an error adding the task. Please try again.")

    # saves the changes to the databse and prints a success message.
    else: 
        conn.commit()
        print(f"The task '{Title}' was added successfully.")

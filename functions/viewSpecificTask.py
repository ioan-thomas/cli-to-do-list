from functions import *

def viewSpecificTask(conn, cursor):

    # SQL query to fetch task
    query = """SELECT TaskID, Title, Details, Dateadded FROM tasks WHERE TaskID = ?"""

    while True:
        try: 
            # ask user for the ID of the task to fetch
            taskID = int(input("What is the ID of the task you'd like to view?: "))

            # executes the query
            cursor.execute(query, taskID)

            # fetching the results from the database
            results = cursor.fetchone()
            print(results)

            # if there are no tasks in the database relating to that taskID
            if results == []:
                print("There are currently nso tasks available. Please add a task and try again.\n")
                return

        # if user attempts to exit the app, the below exitApp function is ran
        except KeyboardInterrupt:
            exitApp()

        # if the user does not enter a number, the below error handling statement will catch the error and ask the user to input a number.
        except ValueError:
            print("Please enter a valid task ID in a number format.\n")

        # catches any other unexpeted errors
        except:
            print("Something went wrong. Please try again later.\n")
            return
        else:
            
            return

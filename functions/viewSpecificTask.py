from functions import *

def viewSpecificTask(conn, cursor):

    # SQL query to fetch task
    query = """SELECT TaskID, Title, Details, Dateadded FROM tasks WHERE TaskID = ?"""

    while True:
        try: 
            # ask user for the ID of the task to fetch
            task_ID = str(input("What is the ID of the task you'd like to view?: "))

            # executes the query
            cursor.execute(query, [task_ID,])

            # fetching the results from the database
            results = cursor.fetchone()

            # if there are no tasks in the database relating to that taskID
            if results == []:
                print("There are currently no tasks available. Plea se add a task and try again.\n")
                return
            
            # if the user enters an invalid ID, they are returned to start and asked for an ID again.
            # try:
            if results == None:
                print("There are no current tasks that meet that criteria.")
            else:
                viewAllDetails([results])

        # if user attempts to exit the app, the below exitApp function is ran
        except KeyboardInterrupt:
            exitApp()

        # if the user does not enter a number, the below error handling statement will catch the error and ask the user to input a number.
        except ValueError:
            print("Please enter a valid task ID in a number format.\n")

        # catches any other unexpeted errors
        except:
            print("Something went wrong. Please contact the developer and try again later.\n")
            return

        else:
                try: 
                    while True:
                        # asks user if they would like to see another task, if yes, loop continues, if not, they are returned to the menu.
                        user_choice = str(input("Would you like to view another task? (Y/N): ")).upper()

                        # loop only breaks if user choice is either yes or no.
                        if user_choice == 'Y':
                            # inner loop breaks, outer loop continues - user is asked for a task ID once again.
                            break

                        if user_choice == 'N':
                            # a stop iteration error is raised, which is caught allowing outer loop to be broken
                            raise StopIteration

                # catches stop iteration errors, breaking out of the loop
                except StopIteration:
                    break

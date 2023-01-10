from functions import *

# creates a tuple with the connect and cursor objects as values - returned from the function. The tuple values reference the tasks.db passed in as a parameter.
db = connectToDatabase('./tasks.db')

def main():
    # this function presents the user with options, asks user for input and runs the relevant function associated with that output.

    # the loop will continue until option 7 is given or the user attempts to exit via the KeyboardInterrupt error.
    while True:
            print("\nPlease select from the following options:")
            print("1. Add a task")
            print("2. View all tasks")
            print("3. View a specific task")
            print("4. Remove a task")  
            print("5. View all removed tasks")
            print("6. Permenantly delete a task")    
            print("7. Update a task")
            print("8. Exit")
            
            try:
                # promts user for decision
                user_choice = int(input("Please enter your choice: "))

                # runs the relevant function associated with the user's output before beginning the loop again until the user either uses the exitApp function or they use the KeyboardInterrupt error to exit the app.
                if user_choice == 1:
                    # runs the function and destructures the db tuple into the connect and cursor objects.
                    addTask(*db) # imported from functions/addTask.py
                if user_choice == 2:
                    # runs the function and destructures the db tuple into the connect and cursor objects. The True parameter presents the user with additional functionality in the viewTasks function.
                    viewTasks(*db, True) # imported from functions/viewTasks.py
                if user_choice == 3:
                    # runs the function and destructures the db tuple into the connect and cursor objects.
                    viewSpecificTask(*db) # imported from functions/viewSpecificTask
                if user_choice == 4:
                    # runs the function and destructures the db tuple into the connect and cursor objects.
                    removeTask(*db) # imported from functions/removeTask.py
                if user_choice == 5:
                    # runs the function and destructures the db tuple into the connect and cursor objects.
                    viewRemovedTasks(*db) # imported from functions/viewRemovedTasks.py
                if user_choice == 6:
                    # runs the function function to delete a specified task and destructures the db tuple into the connect and cursor object.
                    deleteTask(*db)
                if user_choice == 7:
                    # runs the function and destructures the db tuple into the connect and cursor objects.
                    updateTask(*db) # imported from functions/updateTask.py
                if user_choice == 8:
                    # runs the below function to exit the app.
                    exitApp() # imported from functions/exitApp.py
                    
            # if there is a KeyboardInterrupt error, the exitApp function is ran to exit the application.
            except KeyboardInterrupt:
                exitApp()

            except: 
                print('Please enter a number between 1-7')

            # the exception catch all clause needs to be placed after keyboard interrupt

 # sort by date

if __name__ == "__main__":

    # runs the function and destructures the db tuple into the connect and cursor objects.
    createTable(*db) # imported from functions/createTable.py

    # runs the 'main function' i.e. the main menu.
    main()

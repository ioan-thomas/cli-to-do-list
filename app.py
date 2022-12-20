from functions import *

db =connectToDatabase('./tasks.db')

def main():
    # presents the user with options, asks user for input and runs the relevant function associated with that output.

    while True:
        try:
            print("\nPlease select from the following options:")
            print("1. Add a task")
            print("2. View all tasks")
            print("3. Remove a task")  
            print("4. View all removed tasks")
            print("5. Permenantly delete a task")    
            print("6. Update a task")
            print("7. Exit")
            
            # promts user for decision
            user_choice = input("Please enter your choice: ")

            # runs the relevant function associated with the user's output and then breaks out of the loop.
            if user_choice == "1":
                addTask(*db) # imported from functions/addTask.py
            if user_choice == "2":
                viewTasks(*db, True) # imported from functions/viewTasks.py
            if user_choice == "3":
                removeTask(*db) # imported from functions/viewRemovedTasks.py
            if user_choice == "4":
                viewRemovedTasks(*db)
            if user_choice == "5":
                print("5")
            if user_choice == "6":
                updateTask(*db)
            if user_choice == "7":
                exitApp()

        except KeyboardInterrupt:
            exitApp()

 # sort by date

if __name__ == "__main__":

    createTable(*db) # imported from functions/createTable.py

    # runs the 'main function' i.e. the main menu
    main()

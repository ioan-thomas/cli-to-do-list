from functions.exitApp import exitApp

def unremoveTask(conn, cursor):
    # this function set the Removed value in the Tasks table to False. "Unremoving" the task.
    while True:
        try:

            # prompts user for the task ID that they wish to unremove.
            task_ID = int(input("Please enter the taskID you wish to unremove: "))
            
            # the SQL query to be ran. The Removed value associated with the given taskID (in the tasks table) is set to True.  
            query = """UPDATE tasks SET Removed = 0 WHERE TaskID = ?"""

            #executing the SQL query above with the task as the parameter (in place of the "?").
            cursor.execute(query, (task_ID,))

        # if a user does not enter an integer above, the below ValueError will display the message.
        except ValueError:
            print("Please enter a number.")

        # if the user attempts to exit the application, the app will run the exitApp function to do this.
        except KeyboardInterrupt:
            exitApp()
        
        # in the event that something unexpected happens, the app will throw the below error.
        except:
            print("Something went wrong. Please check the taskID you are trying to use and try again.")

        else: 
              # commits the changes to the tasks database and presents the user with the message.
            conn.commit()
            print("That task has been unremoved. Please return to the main menu and select option 2 to view all tasks.\n ")

            # prompts user for decision if they would like to remove another task or return to main menu
            user_choice = str(input("Would you like to unremove another task? (Y/N): ")).upper()

            # returns user to main menu
            if user_choice == 'N':
                return

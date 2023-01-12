from functions.viewAllDetails import viewAllDetails
from functions.exitApp import exitApp

def viewTasks(conn, cursor, viewDetails, abilityToSort):
    # this function is used to view all tasks that have not been removed from the database and sort them by the user's decision.

    try: 
        sortby= "TaskID"
        orderby = "ASC"
        

        if abilityToSort == True:
            decisionToOrderBy = None

            while decisionToOrderBy not in range(1, 7):
                print("\nPlease select from the following options: ")
                print("1. Order by Title Alphabetically [Ascending]")
                print("2. Order by Title Alphabetically [Descending]")
                print("3. Order by Date Added Alphabetically [Ascending]")
                print("4. Order by Date Added Alphabetically [Descending]")
                print("5. Order by Task ID [Ascending]")
                print("6. Order by Task ID [Descending]")

                decisionToOrderBy = int(input("\nHow would you like to sort the the results?: "))

            # ordering the results by the user's decision
            if decisionToOrderBy == 1 or decisionToOrderBy == 2:
                sortby = 'Title'
            if decisionToOrderBy == 2 or decisionToOrderBy == 4 or decisionToOrderBy == 6:
                orderby = 'DESC'
            if decisionToOrderBy == 3 or decisionToOrderBy == 4:
                sortby = 'Dateadded'

        # assembling the query with the sortby and orderby parameters
        query = """SELECT TaskID, Title, Details, Dateadded FROM tasks WHERE Removed = 0 ORDER BY {} {}""".format(sortby, orderby)

        # executing the query with the sortby and orderby parameters
        cursor.execute(query)

        # fetching all of the results from the database into a list.
        results = cursor.fetchall()

        # if the list is empty, the below message is shown in the console and the user is returned to main function that called this viewTasks function.
        if results == []:
            print("\n There aren't any tasks yet.")
            return -1

        # printing all of the results to the console. 
        print("Here are all the tasks:\n")
        print(results)
        for task in results: 
            print(f"""\n{task[0]}: {task[1]}\n""")
        

        # the viewDetails parameter allows for added functionality within this function. If the user should be given the option to view more details about the task then the below code is ran.
        # the user is prompted whether or not they would like to view more details. If the user selects yes then the viewAllDetails function is ran displaying those details. If not, the user is returned to the main() function which is where this viewTasks function was called.
        if viewDetails:
            while True:
                try:
                    user_choice = str(input("Would you like to view all task details? (Y/N): ")).upper()

                    if user_choice == 'N':
                        raise StopIteration
                    if user_choice == 'Y':
                        viewAllDetails(results)
                        raise StopIteration
                except StopIteration:
                    break
    except ValueError:
        print("Please enter a valid number.")

    except TypeError:
        print("Please enter a valid number.") 

    except KeyboardInterrupt:
        exitApp()
    
    except Exception as e:
        print("An error occurred. Please try again later.")
        print(e)

import sqlite3

# connecting to the database / creating one if it does not exist.

# this function allows for any arugment to be supplied (databasePath) so the app to be expanded in future if need be.

def connectToDatabase(database_path):
    # creating a reference to the connection and cursor objects - for the supplied database (via databasePath argument).
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # returning a tuple containing the above objects to be used in other functions without needing to repeat code.
    return (conn, cursor)


import sqlite3

# connecting to the database / creating one if it does not exist.

# allowing for any arugment to be supplied (databasePath) allows for the app to be expanded in future if need be.

def connectToDatabase(databasePath):
    conn = sqlite3.connect(databasePath)
    cursor = conn.cursor()

    return (conn, cursor)


# can you make two of the same name?

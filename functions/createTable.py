def createTable(conn, cursor):
    # this function creates a table in the database if it doesn't already exist

    # creating a variable containing the SQL query to be run. The NOT NULL ensures no values in the database are a value of null as this ensures all values are correct - allowing for a smooth application by producing errors to handle and display to the user.
    query = """CREATE TABLE tasks 
    (TaskID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Title(100) TEXT NOT NULL,
    Details(250) TEXT NOT NULL,
    Dateadded TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Removed BOOLEAN NOT NULL DEFAULT FALSE)"""

    # the TaskID value must be an integer and will act as the primary key for the database inputs - this is important as it allows records to be uniquely identifiable.
    # The Title and Details entries must be of a text value (a string).
    # The Dateadded is of a TIMESTAMP value which means it will be in a date form (e.g. dd-mm-yyyy) and defaults to the current time (which will be when the entry is commited to the database).
    # The Removed value is a BOOLEAN (i.e. only True or False / 1 or 0 in the case of SQL) and defaults to FALSE (i.e. 0 in SQL) as all values must be shown as not removed when commited to the database.

    # attempts to create the table using the above query but shows a message if one already exists
    try: 
        cursor.execute(query)
        conn.commit()
    except:
        print("Database table already exists.")


def createTable(conn, cursor):
    # this function creates a table in the database if it doesn't already exist

    # the SQL query to be run 
    query = """CREATE TABLE tasks
    (TaskID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Title TEXT NOT NULL,
    Details TEXT NOT NULL,
    Dateadded TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Removed BOOLEAN NOT NULL DEFAULT FALSE)"""

    # attempts to create the table using the above query but shows a message if one already exists
    try: 
        cursor.execute(query)
        conn.commit()
    except:
        print("Database table already exists.")

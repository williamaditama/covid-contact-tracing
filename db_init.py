import sqlite3

try:
    sqliteConnection = sqlite3.connect('database.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

############################################
    cursor.execute('CREATE TABLE users (uuid TEXT)')
    cursor.execute('CREATE TABLE locations (userID TEXT, lat DECIMAL, lng DECIMAL, timestamp INTEGER)')
############################################

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

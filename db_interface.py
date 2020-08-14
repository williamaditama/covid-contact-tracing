import sqlite3

def connect():
    return

def add_user(uuid):
    connection = sqlite3.connect('database.db')
    connection.execute(f'INSERT INTO users VALUES (?)', (uuid))

def add_loc(userID, lat, lng, timestamp):
    connection = sqlite3.connect('database.db')
    query = "INSERT INTO locations VALUES (?, ?, ?, ?)"
    connection.execute(query, (userID, lat, lng, timestamp))
    connection.commit()

def get_loc():
    connection = sqlite3.connect('database.db')

    result = connection.execute('SELECT * FROM locations')
    out = result.fetchall()
    #out is a list of tuples with each row = 1 tuple
    return out

import sqlite3
import os


def connect():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return sqlite3.connect(os.path.join(dir_path, 'database.db'))

def add_user(uuid):
    connection = connect()
    connection.execute(f'INSERT INTO users VALUES (?)', (uuid))

def add_loc(userID, lat, lng, timestamp):
    connection = connect()
    query = "INSERT INTO locations VALUES (?, ?, ?, ?)"
    connection.execute(query, (userID, lat, lng, timestamp))
    connection.commit()

def get_loc():
    connection = connect()

    result = connection.execute('SELECT * FROM locations')
    out = result.fetchall()
    #out is a list of tuples with each row = 1 tuple
    return out

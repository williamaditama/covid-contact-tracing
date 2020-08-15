import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def connect():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

def add_user(uuid):
    connection = connect()
    connection.cursor().execute('INSERT INTO users VALUES (%s)', (uuid,))
    connection.commit()

def add_loc(userID, lat, lng, timestamp):
    connection = connect()
    query = "INSERT INTO locations VALUES (%s, %s, %s, %s)"
    connection.cursor().execute(query, (userID, lat, lng, timestamp))
    connection.commit()

def get_loc():
    connection = connect()

    result = connection.execute('SELECT * FROM locations')
    out = result.fetchall()
    #out is a list of tuples with each row = 1 tuple
    return out

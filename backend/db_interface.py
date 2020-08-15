import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def connect():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

def add_user(uuid):
    connection = connect()
    try:
        connection.cursor().execute('INSERT INTO users VALUES (%s)', (uuid,))
        connection.commit()
    except psycopg2.errors.InFailedSqlTransaction:
        connection.rollback()

def add_loc(userID, lat, lng, timestamp):
    connection = connect()
    try:
        query = "INSERT INTO locations VALUES (%s, %s, %s, %s)"
        connection.cursor().execute(query, (userID, lat, lng, timestamp))
        connection.commit()
    except psycopg2.errors.InFailedSqlTransaction:
        connection.rollback()

def get_loc():
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM locations')
    out = cursor.fetchall()
    #out is a list of tuples with each row = 1 tuple
    return out

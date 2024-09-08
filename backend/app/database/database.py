import psycopg2
from flask import Flask

app = Flask(__name__)

#Database connection
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname = "Laundry Decider",
            user = "postgres",
            password = "postgres",
            host = "localhost",
            port = "5432"
        )
        cursor = conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to the Database", error)

#Close database connection properly
def close_db(conn, cursor):
        cursor.close()
        conn.close()

import psycopg2
from flask import Blueprint

database_bp = Blueprint('database', __name__)

#Database connection
@database_bp.route('/connect_db', methods=['POST'])
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

        return cursor

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to the Database", error)

#Close database connection properly
@database_bp.route('/close_db', methods=['GET'])
def close_db(conn, cursor):
        cursor.close()
        conn.close()

#Question - do I need to use Blueprint here? Do I need to decorate my functions to 
# connect/close the DB? Or can I remove the decorators, and just import my functins in the 
#innit file?

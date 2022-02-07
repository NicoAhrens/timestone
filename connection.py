import psycopg2
from config import config


def connect():
    # ======= Connect to the PostgreSQL databse server =======

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print(f'Connecting to the PostgreSQL server {params["database"]}...')
        # ** before a paramter is a sign of the function getting more than one
        # argument from a dictionary (in this case the username, password etc.)
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            conn.close()
            print('Database connection closed.')


def single_command(command):
    conn = None
    try:
        # connecting to the database and creating a cursor
        params = config()
        # connect to the PostgreSQL server
        print(f'Connecting to the PostgreSQL server {params["database"]}...')
        # ** before a paramter is a sign of the function getting more than one
        # argument from a dictionary (in this case the username, password etc.)
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
        cur.execute(command)
        # closes the connection
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            conn.close()


def fetch_information(command):
    pass

if __name__ == '__main__':
    connect()

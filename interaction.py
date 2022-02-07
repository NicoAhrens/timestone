# System libraries
from datetime import datetime as dt
# Installed libraries
import psycopg2

# Own libraries
from connection import single_command
from config import config


def delete_entry():
    pass


def update_entry():
    pass


def calculate_time():
    command = (
                f"""
                [PSQL CODE BLOCK];
                """
                )
    single_command(command)

    return print(worked_time)

if __name__ == '__main__':
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
        # Creating a query for the database
        date = "2022-02-07"
        # TODO: Create another column in table with the name deltatimesec and 
        # everytime a new entry is added, calculate the difference between the 
        # two times or timeframes
        query =(
        f"""
        SELECT
            date,
            time,
            entry_id,
            status_id,
            time - lag(time) OVER (ORDER BY entry_id) as increase
        FROM timekeeping;
        """)

        cur.execute(query)
        # # commit the changes
        # conn.commit()

        print(f"Selecting rows from timekeeping using cursor.fetchone")
        logged_events = cur.fetchall()
        
        print(logged_events)
        # print("Print each row and it's columns values")
        # for row in mobile_records:
        #     print("Id = ", row[0], )
        #     print("Model = ", row[1])
        #     print("Price  = ", row[2], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")

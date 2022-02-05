import psycopg2
from config import config
from os import datetime


# TODO: Create a function who gets the time es an input and dependen on the input
# of the user connect with other commands over psycopg2
# create a query for the user to look up specific times and dates to update or
# correct and also calculate the worked time on that day
# and calulate for the week and month and year
# Maybe hours minutes seconds , year month and day have to have each a column
def timestone():
    # ======= Creates necessary tables in the database =======
    escape = False
    while escape:
        print()
        print("'i' to stamp your login time.")
        print("'o' to stamp your logout time.")
        print("'bo' to stamp out for a break.")
        print("'bi' to stamp in after a break.")
        print("q for quitting the programm")
        print()
        print('> ')
        user_input = input().lower()
        if user_input == 'q':
            escape = True
        elif user_input == 'i':
            pass
        elif user_input == 'o':
            pass
        elif user_input == 'bo':
            pass
        elif user_input == 'bi':
            pass
    commands = (
        f"""
        INSERT INTO employee(time)
        VALUES ('{fname_employee}', '{lname_employee}')
        RETURNING *;
        """
        )
    print(commands)
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

        for command in commands:
            cur.execute(command)
        # closes the connection
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    timestamp()

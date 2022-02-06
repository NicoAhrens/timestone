import psycopg2
from config import config


def create_employee():
    # ======= Creates necessary tables in the database =======
    # Commands for creating the tables with the cols
    fname_employee = input('First name of employee: ')
    lname_employee = input('Last name of employee: ')
    # print(f'{lname_employee}, {fname_employee}')
    command = (
        f"""
        INSERT INTO employee(first_name, last_name)
        VALUES ('{fname_employee}', '{lname_employee}');
        """
        )
    # print(command)
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
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_employee()

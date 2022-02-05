import psycopg2
from config import config


def create_tables():
    # ======= Creates necessary tables in the database =======
    # Commands for creating the tables with the cols
    commands = (
        """
        DROP TABLE IF EXISTS employee CASCADE;
        DROP TABLE IF EXISTS status CASCADE;
        DROP TABLE IF EXISTS timekeeping CASCADE;
        CREATE TABLE employee(
            employee_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255)
        )
        """,
        """
        CREATE TABLE status(
            status_id SERIAL PRIMARY KEY,
            status_name VARCHAR(255)
            )
        """,
        """
        INSERT INTO status(status_name)
        VALUES ('work_in')
        RETURNING *;
        INSERT INTO status(status_name)
        VALUES ('work_out')
        RETURNING *;
        INSERT INTO status(status_name)
        VALUES ('break_in')
        RETURNING *;
        INSERT INTO status(status_name)
        VALUES ('break_out')
        RETURNING *;
        """,
        """
        CREATE TABLE timekeeping(
            entry_id SERIAL PRIMARY KEY,
            time_stamp TIMESTAMP,
            employee_id SERIAL,
            status_id SERIAL,
            FOREIGN KEY (employee_id)
                REFERENCES employee (employee_id)
                 ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (status_id)
                REFERENCES status (status_id)
                ON UPDATE CASCADE ON DELETE CASCADE
            )
        """
        )
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
    create_tables()

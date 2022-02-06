import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import config


# TODO: User which is created save into the database.ini onto the right place
# with Config.Parser.write().
def initialize_db_and_tbl():
    # ======= Creates necessary database and tables =======
    # Commands for creating the tables with the cols
    new_user = input('Which username for the database, do you want to set: ')
    password = input('Which password for the user do you want to set: ')
    commands = (
        f"""
        DO
        $do$
        BEGIN
           IF NOT EXISTS (
              SELECT FROM pg_catalog.pg_roles
              WHERE  rolname = '{new_user}') THEN
              CREATE ROLE {new_user} SUPERUSER LOGIN PASSWORD '{password}';
           END IF;
        END
        $do$;
        """,
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
        # connecting to the default database and creating a cursor
        params = config(filename='database_init.ini', section='postgresql')
        # connect to the PostgreSQL server
        print("Connecting to the PostgreSQL server and the DATABASE "
              f"{params['database']}...")
        # ** before a paramter is a sign of the function getting more than one
        # argument from a dictionary (in this case the username, password etc.)
        conn = psycopg2.connect(**params)
        # autocmmit for DROP DATABASE in execute()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # create a cursor
        cur = conn.cursor()
        # Deleting the timestone DATABASE IF it exists
        user_input = input("Do you really want to delete the DATABASE "
                           "timestone? [y/n]\n> ")
        if user_input == "y":
            cur.execute('DROP DATABASE IF EXISTS timestone;')
            cur.execute('CREATE DATABASE timestone;')
            cur.close()
            conn.commit()
        else:
            print("Keeping DATABASE timestone")
            cur.close()
        # connecting to the database and creating a cursor
        params = config()
        # connect to the PostgreSQL server
        print("Connecting to the PostgreSQL server and the DATABASE "
              f"{params['database']}...")
        # ** before a paramter is a sign of the function getting more than one
        # argument from a dictionary (in this case the username, password etc.)
        conn = psycopg2.connect(**params)
        # autocmmit for DROP DATABASE in execute()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
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
    initialize_db_and_tbl()

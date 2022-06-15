# System libraries
from datetime import datetime
import os
from os import get_terminal_size as gts

# Installed libraries
# import keyboard

# Own libraries
from config import config
from connection import single_command


# TODO: Create a function which gets the time es an input and dependend on the
# input of the user, connects with the postgreSQL Databse over the psycopg2
# library. Creates a query for the user to look up specific times and dates to
# update, correct or calculate the worked time on that date.


def start_screen():
    """
   Printing the Start Screen/Logo
    -----
    Parameters:
        None
    Returns:
        None
    """
    lines =\
        [
            "",
            ("⬗ TIMESTONE ⬖\n").center(gts().columns),
            ("Keeping track of your time!").center(gts().columns), "\n"
        ]
    for line in lines:
        print(line)


def main_menu():
    """
    Printing out the menu
    -----
    Parameters:
        None
    Returns:
        None
    """
    options =\
        [
            "Press [1]: Start Main Programm",
            "Press [2]: Calculations",
            "Press [X]: Quit the Programm"
        ]
    for option in options:
        print(option)


def logging_menu():
    """
    Printing out the menu
    -----
    Parameters:
        None
    Returns:
        None
    """

    terminal_width = gts().columns
    options =\
        [
            "",
            "◈"*terminal_width,
            "",
            "Press [I]: Stamp in",
            "Press [O]: Stamp out",
            "Press [B]: Stamp out for break",
            "Press [L]: Stamp in after break",
            "Press [X]: Quit to Main Menu",
            "Press [Q]: Quitting Timestone"
        ]
    for option in options:
        print(option)


def calculations_menu():
    """
    Printing out the menu for calculations
    -----
    Parameters:
        None
    Returns:
        None
    """
    terminal_width = gts().columns
    options =\
        [
            " ",
            "◈"*terminal_width,
            " ",
            "Press [A]: Worked time in an specific intervall",
            "Press [B]: Worked time on a specific day",
            "Press [X]: Quit to Main Menu",
            "Press [Q]: Quitting Timestone"
        ]
    for option in options:
        print(option)


def clearConsole():
    """
   Clear the displayed console
    -----
    Parameters:
        None
    Returns:
        None
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def log_event(date, time, status_id):
    """
    Printing out the menu
    -----
    Parameters:
        date []
        time []
        status_id []
    Returns:
        None
    """
    command = (
                f"""
                INSERT INTO timekeeping(date, time, employee_id, status_id)
                VALUES ('{date}', '{time}', '1', '{status_id}');
                """
                )
    single_command(command)


def log_date_time():
    """
    Gets the date and time from a timestamp
    -----
    Parameters:
        None
    Returns:
        date [str]: Stripped date from the timestamp
        time [str]: Stripped time from the timestamp
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp_split = timestamp.split()
    date = timestamp_split[0]
    time = timestamp_split[1]
    return date, time

def timestamp():
    """
    Workflow
    -----
    Parameters:
        None
    Returns:
        None
    """
    # ======= Creates necessary tables in the database =======
    command = None
    timestamp = None
    status_id = None
    esc_main = False
    esc_timekeeping = False
    esc_calc = False
    clearConsole()

    while not esc_main:
        start_screen()
        main_menu()
        user_input_main = input("> ").lower()
        if user_input_main == 'x':
            break
        elif user_input_main == '2':
            calculations_menu()
            while not esc_calc:
                user_input_calc = input("> ").lower()
                if user_input_calc == "a":
                    pass
                elif user_input_calc == 'q':
                    esc_main = True
                    esc_calc = True
                    print('Quitting Timestone. \nUntil next time!')
                elif user_input_calc == 'x':
                    esc_calc = True
                    print('Quitting to Main Menu...')
        elif user_input_main == '1':
            logging_menu()
            while not esc_timekeeping:
                user_input_log = input("> ")

                if user_input_log == 'i':
                    date, time = log_date_time()
                    status_id = '1'
                    print('Logged in.')
                    print(f"Stamped in Date: {date} and Time: {time}")
                    log_event(date, time, status_id)
                elif user_input_log == 'o':
                    date, time = log_date_time()
                    status_id = '2'
                    print('Logged out.')
                    log_event(date, time, status_id)
                elif user_input_log == 'b':
                    date, time = log_date_time()
                    status_id = '3'
                    print('Logged into break. Enjoy your meal! :)')
                    log_event(date, time, status_id)
                elif user_input_log == 'l':
                    date, time = log_date_time()
                    status_id = '4'
                    print('Logged out of break. Hope you enjoyed your meal. :)')
                    log_event(date, time, status_id)
                elif user_input_log == 'q':
                    esc_main = True
                    esc_timekeeping = True
                    print('Quitting Timestone. \nUntil next time!')
                elif user_input_log == 'x':
                    esc_timekeeping = True
                    print('Quitting to Main Menu...')


if __name__ == '__main__':
    timestamp()

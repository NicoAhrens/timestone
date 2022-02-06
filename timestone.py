# System libraries
from datetime import datetime
import os
from os import get_terminal_size as gts

# Installed libraries
import keyboard

# Own libraries
from config import config
from connection import single_command


# TODO: Create a function who gets the time es an input and dependen on the
# input of the user connect with other commands over psycopg2
# create a query for the user to look up specific times and dates to update or
# correct and also calculate the worked time on that day
# and calulate for the week and month and year
# Maybe hours minutes seconds , year month and day have to have each a column


def start_screen():
    lines =\
        [
            "",
            ("⬗ TIMESTONE ⬖\n").center(gts().columns),
            ("Keeping track of your time!").center(gts().columns), "\n",
            ("Press Enter").center(gts().columns)
        ]
    for line in lines:
        print(line)


def main_menu():
    options =\
        [
            "Press '1': Start Main Programm",
            "Press '2': Calculations",
            "Press 'X': Quit the Programm"
        ]
    # clearConsole()
    for option in options:
        print(option)


def logging_menu():
    terminal_width = gts().columns
    options =\
        [
            ""
            "◈"*terminal_width,
            "Press 'I': Stamp in",
            "Press 'O': Stamp out",
            "Press 'B': Stamp out for break",
            "Press 'L': Stamp in after break",
            "Press 'X': Quit the timekeeping"
        ]
    for option in options:
        print(option)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# TODO: revert to state beforehand
def keypress(press_key):
    while True:
        try:
            keyboard.is_pressed(press_key)
            return press_key
            # if keyboard.is_pressed('i'):
            #     return 'i'
            # elif keyboard.is_pressed('o'):
            #     return 'o'
            # elif keyboard.is_pressed('b'):
            #     return 'b'
            # elif keyboard.is_pressed('l'):
            #     return 'l'
            # elif keyboard.is_pressed('x'):
            #     return 'x'
            # elif keyboard.is_pressed('1'):
            #     return '1'
            # elif keyboard.is_pressed('2'):
            #     return '2'
            # elif keyboard.is_pressed('3'):
            #     return '3'
        except KeyboardError:
            raise Exception('Wrong input')  # if user pressed a key other than the given key the loop will break


def log_event(timestamp, status_id):
    command = (
                f"""
                INSERT INTO timekeeping(time_stamp, employee_id, status_id)
                VALUES ('{timestamp}', '1', '{status_id}');
                """
                )
    # print(command)
    single_command(command)

def timestamp():
    # ======= Creates necessary tables in the database =======
    # create a parser
    # dict_ini = config()
    # Create a controller to catch key presses of user
    command = None
    # print(dict_ini)
    # employee = dict_ini['user']
    timestamp = None
    status_id = None
    escape_main = False
    clearConsole()
    while not escape_main:
        start_screen()
        keyboard.wait('enter')
        main_menu()
        key = input().lower()
        keypress(key)
        if user_input == 'x':
            break
        elif user_input == '2':
            pass
        elif user_input == '1':
            escape_timekeeping = False
            while not escape_timekeeping:
                logging_menu()
                key = None
                while not key:
                    key = input().lower()
                    keypress(key)
                #user_input = keypress()
                if user_input == 'i':
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status_id = '1'
                    print('Logged in.')
                    log_event(timestamp, status_id)
                elif user_input == 'o':
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status_id = '2'
                    print('Logged out.')
                    log_event(timestamp, status_id)
                elif user_input == 'b':
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status_id = '3'
                    print('Logged into break. Enjoy your meal! :)')
                    log_event(timestamp, status_id)
                elif user_input == 'l':
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status_id = '4'
                    print('Logged out of break. Hope you enjoyed your meal. :)')
                    log_event(timestamp, status_id)
                elif user_input == 'x':
                    escape_timekeeping = True
                    print('Will quit the programm. Goodbye.')
                    log_event(timestamp, status_id)


if __name__ == '__main__':
    timestamp()

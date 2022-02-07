# System libraries
from datetime import datetime
import os
from os import get_terminal_size as gts

# Installed libraries
# import keyboard

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
            "Press 'X': Quit to Main Menu",
            "Press 'Q': Quitting Timestone"
        ]
    for option in options:
        print(option)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# TODO: Mabye without package keyboard. Have to look into it how it really works
# def keypress():
#     while True:
#         try:
#             if keyboard.is_pressed('i'):
#                 return 'i'
#             elif keyboard.is_pressed('o'):
#                 return 'o'
#             elif keyboard.is_pressed('b'):
#                 return 'b'
#             elif keyboard.is_pressed('l'):
#                 return 'l'
#             elif keyboard.is_pressed('q'):
#                 return 'q'
#             elif keyboard.is_pressed('x'):
#                 return 'x'
#             elif keyboard.is_pressed('1'):
#                 return '1'
#             elif keyboard.is_pressed('2'):
#                 return '2'
#             elif keyboard.is_pressed('3'):
#                 return '3'
#         except KeyboardError:
#             raise Exception('Wrong input')  # if user pressed a key other than the given key the loop will break


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
    escape_timekeeping = False
    clearConsole()
    while not escape_main:
        start_screen()
        #keyboard.wait('enter')
        main_menu()
        user_input_main = input("> ")
        # user_input_main = keypress()
        if user_input_main == 'x':
            break
        elif user_input_main == '2':
            pass
        elif user_input_main == '1':
            logging_menu()
            while not escape_timekeeping:
                user_input_log = input("> ")
                # user_input_log = keypress()
                # user_input = keypress()ii
                if user_input_log == 'i':
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status_id = '1'
                    print('Logged in.')
                    log_event(timestamp, status_id)
                elif user_input_log == 'o':
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status_id = '2'
                    print('Logged out.')
                    log_event(timestamp, status_id)
                elif user_input_log == 'b':
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status_id = '3'
                    print('Logged into break. Enjoy your meal! :)')
                    log_event(timestamp, status_id)
                elif user_input_log == 'l':
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status_id = '4'
                    print('Logged out of break. Hope you enjoyed your meal. :)')
                    log_event(timestamp, status_id)
                elif user_input_log == 'q':
                    escape_main = True
                    escape_timekeeping = True
                    print('Quitting Timestone. \nUntil next time!')
                elif user_input_log == 'x':
                    escape_timekeeping = True
                    print('Quitting to Main Menu...')


if __name__ == '__main__':
    timestamp()

# Timestone

What does this do?
Logs times in a postgreSQL Database. Can keep track of your working time and how many breaks you had and how long they took.

Dependencies: 
# pip install keyboard
# pip install psycopg2
# pip install postgreSQL

How to run:
You have to run the script with:
sudo python3 timestone.py 
Because the packages 'keyboard' needs root to track keyboard presses.
If you are using a conda enviroment the sudo python3 doesn't find your packages you installed for the enviroment, even if you found it. 
My workaround right now is:
$ sudo env "PATH=$PATH" python3 timestone.py

First create an employee/user with "create_employee.py"

# Timestone

What does this do?
Logs times in a postgreSQL Database. Can keep track of your working time and how many breaks you had and how long they took.

## Dependencies: 
`$ pip install psycopg2` <br \>
`$ pip install postgreSQL`

## How to Use:
1. First you have to install the dependencies above.
2. Create a starting database in postgreSQL.
3. Change the `user=nico` to your postgreSQL user name.
4. Initialize the database with `initialize_database.py`.
5. Create a employee name with `create_employee.py` to log the time and date for a specific user. (Change the ID of the user in `timestone.py` accordingly, if another user is the same script.)
6. Start the programm with `timestone.py`. 


## Future Implementations:
- [ ] Adding another column in the database to better track the worked time from the previous logged event.
- [ ] Calculating the worked time on a specific day, week, month year. 
- [ ] Updating/Correcting values in the database.
- [ ] Search for specific dates to show every logged event on that day.
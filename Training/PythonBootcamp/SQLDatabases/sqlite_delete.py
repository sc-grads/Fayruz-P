## Working with Sqlite Databases in Python
## Deleting records
#################################

## Importing the module
import sqlite3

## Opening the connection to the database (if it exists) or create the db if it doesn't exist
connection = sqlite3.connect('my_database.db')

## Creating a cursor object
cursor = connection.cursor()

## User enters a department:
department = input('Department:')

## Deleting all records with the department entered by the user. This is parameterized query.
sql = 'DELETE FROM employees where department = ?;'
cursor.execute(sql, (department,))

## Committing the changes
connection.commit()

## Closing the connection to the database
connection.close()
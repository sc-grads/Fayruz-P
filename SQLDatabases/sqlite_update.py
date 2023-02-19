## Working with Sqlite Databases in Python
## Updating records in a table
#################################

## Importing the module
import sqlite3

## Opening the connection to the database (if it exists) or create the db if it doesn't exist
connection = sqlite3.connect('my_database.db')

## Creating a cursor object
cursor = connection.cursor()

## User enters an ID:
id = input('Id:')

## Updating the record with the ID entered by the user. This is parameterized query.
sql = 'UPDATE employees SET department="Sales" where id=?;'
cursor.execute(sql, (id,))

## Committing the changes
connection.commit()

## Closing the connection to the database
connection.close()  #################################
## Working with Sqlite Databases in Python
## Updating records in a table
#################################

## Importing the module
import sqlite3

## Opening the connection to the database (if it exists) or create the db if it doesn't exist
connection = sqlite3.connect('my_database.db')

## Creating a cursor object
cursor = connection.cursor()

## User enters an ID:
id = input('Id:')

## Updating the record with the ID entered by the user. This is parameterized query.
sql = 'UPDATE employees SET department="Sales" where id=?;'
cursor.execute(sql, (id,))

## Committing the changes
connection.commit()

## Closing the connection to the database
connection.close()
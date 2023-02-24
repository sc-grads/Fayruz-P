## Working with Sqlite Databases in Python
## Selecting data from a table
#################################

## Importing the module
import sqlite3

## Opening the connection to the database (if it exists) or create the db if it doesn't exist
connection = sqlite3.connect('my_database.db')

## Creating a cursor object
cursor = connection.cursor()

## Creating the sql statement
sql = 'select * from employees'

## A more complex sql select statement
## sql = 'select * from employees where name LIKE "A%" order by name desc'


## Execute the sql against the database (db)
cursor.execute(sql)

## Iterating over the result and printing each record of the table
for row in cursor.fetchall():
    print(row)

## Committing the changes (if any)
connection.commit()

## Closing the connection to the database
connection.close()
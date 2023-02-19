## Working with Sqlite Databases in Python
## Parameterized Queries
#################################

## Importing the module
import sqlite3

## Opening the connection to the database (if it exists) or create the db if it doesn't exist
connection = sqlite3.connect('my_database.db')

## Creating a cursor object
cursor = connection.cursor()

## User enters an ID:
id = input('Enter ID:')

## Select the record with the ID entered by the user
## ? is placeholder, will be replaced with id entered by the user
sql = 'select * from employees where id = ?;'

## Execute the sql against the database (db)
## The second argument is a tuple. Each element of the tuple will replace a ? in the sql statement.
cursor.execute(sql, (id,))

## Iterating over the result and printing each record of the table
for row in cursor.fetchall():
    print(row)

## A 2nd example. Inserting a new record

## Creating a new record as a tuple
record = (10, 'Leonardo Romano', 'Marketing', '+40122111', 'leo@x.com')

## Creating the sql statement. Each ? will be replaces with an item of the tuple
sql = 'insert into employees values (?,?,?,?,?);'

## The second argument is a tuple. Each element of the tuple will replace a ? in the sql statement.
cursor.execute(sql, record)

## Committing the changes
connection.commit()

## Closing the connection to the database
connection.close()
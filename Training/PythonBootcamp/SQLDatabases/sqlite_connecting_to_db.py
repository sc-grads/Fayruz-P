## Working with Sqlite Databases in Python
## Connecting to an Sqlite DB and Creating Tables with Python
#################################

## Importing the module
import sqlite3

## Opening the connection to the database (if it exists) or create the db if it doesn't exist
connection = sqlite3.connect('my_database.db')

## Creating a cursor object
c = connection.cursor()

## Creating an Sql Statement as a multiline string
## This sql creates a table with 5 fields (columns)
sql = """
        CREATE TABLE IF NOT EXISTS employees (
         id INTEGER,
         name VARCHAR(64),
         department VARCHAR(32),
         phone VARCHAR(16),
         email VARCHAR(32)
        )
        """

## Execute the sql against the database (db)
c.execute(sql)

## Committing the changes
connection.commit()

## Closing the connection to the database
connection.close()
## Working with Sqlite Databases in Python
## Inserting into a table of a database
#################################

## Importing the module
import sqlite3

## Opening the connection to the database (if it exists) or create the db if it doesn't exist
connection = sqlite3.connect('my_database.db')

## Creating a cursor object
cursor = connection.cursor()

## Creating Sql Statements as a multiline string
## These Sql statements insert 3 records in employees table
sql = """
INSERT INTO employees (id, name, department, phone, email) VALUES (1, "John Smith", "IT", "+123456789", "johns@mycompany.com");
INSERT INTO employees VALUES (2, "Anne Barker", "Accounting", "+155345789", "anne@mycompany.com");
INSERT INTO employees VALUES (3, "Antony Winter", "Sales", "0042345678911", "danw@mycompany.com");
"""

## Call executescript() when executing more sql statements and execute() when executing a single sql statement


## Execute the sql statements against the database
cursor.executescript(sql)

## Committing the changes
connection.commit()

## Closing the connection to the database
connection.close()
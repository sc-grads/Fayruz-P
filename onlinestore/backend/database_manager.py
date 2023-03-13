import pyodbc

server = 'DESKTOP-ISR70S1'
database = 'Spicelet'
username = 'ecommercedbuser'
password = 'ecommerceDBuser1!'
driver = 'ODBC Driver 17 for SQL Server'

connection = f'''DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};'''

def conn():

    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute('select @@SERVERNAME')
    cursor.fetchall()
    return 'Connected'



print(conn())
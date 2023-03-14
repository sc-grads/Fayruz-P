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


def insert(fname, lname, email,newpassword,number ,address):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute(f"Insert into Customers(first_name,last_name,email_address,password,contact_no,address) VALUES('{fname}', '{lname}', '{email}','{newpassword}','{number}' ,'{address}')")
    cursor.commit()
    cursor.close()
    return 'Added User'

# insert('Fayruz','Paruk','fayruz.p@gmail.com','12345','0792480727','12 Bird Street')
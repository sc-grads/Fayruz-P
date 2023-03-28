import pyodbc
from flask import Flask, request, session, jsonify

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


def insert(fname, lname, email, newpassword, number, address):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute(
        f"Insert into Customers(first_name,last_name,email_address,password,contact_no,address) VALUES('{fname}', '{lname}', '{email}','{newpassword}','{number}' ,'{address}')")
    cursor.commit()
    cursor.close()
    return 'Added User'

def retrieve(username, newpassword):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute('SELECT * FROM Customers WHERE email_address = ? AND password = ?', (username, newpassword))
    row = cursor.fetchone()
    if row:
        # TODO: generate and return a token or session variable
        session['customer_ID'] = row.id
        return jsonify({'success': True, 'message': 'Logged in'})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'})


def profile():
    user_id = session.get('customer_ID_id')

    if user_id is None:
        return 'Unauthorized', 401
    else:
        dbconnect = pyodbc.connect(connection)
        cursor = dbconnect.cursor()
        cursor.execute('SELECT * FROM Customers WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        cursor.close()

        return jsonify({'username': user.username, 'email': user.email})

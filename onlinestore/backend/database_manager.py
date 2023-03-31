from collections import namedtuple
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

        session['customer_ID'] = row.id
        return jsonify({'success': True, 'message': 'Logged in'})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'})




def get_products():
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute("SELECT product_ID, product_name, product_price, product_size FROM Products")
    rows = cursor.fetchall()
    Product = namedtuple('Product', [column[0] for column in cursor.description])
    return [dict(Product._make(row)._asdict()) for row in rows]





def add_to_cart(product_ID, quantity):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute("INSERT INTO Cart (product_id, quantity) VALUES (?, ?)", (product_ID, quantity))
    cursor.commit()
    cursor.close()
    return jsonify({'message': 'Item added to cart'})


def get_cart():
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute(
        "SELECT Products.product_name, Products.product_price, Cart.quantity, Products.product_ID FROM Cart INNER JOIN Products ON "
        "Cart.product_ID=Products.product_ID")
    cart_items = cursor.fetchall()
    Items = namedtuple('CartItem', [column[0] for column in cursor.description])
    items_dict = [dict(Items._make(row)._asdict()) for row in cart_items]
    cursor.close()

    return items_dict

def remove_from_cart(product_ID):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute("DELETE FROM Cart WHERE product_ID=?", (product_ID,))
    dbconnect.commit()
    cursor.close()






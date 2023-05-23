import binascii
import os
from collections import namedtuple
import pyodbc
from flask import Flask, request, jsonify
import bcrypt
from bcrypt import hashpw, gensalt, checkpw as safe_checkpw


server = 'DESKTOP-ISR70S1'
database = 'SPICELET_STORE'
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


def insert_product(product_name, product_price, product_weight, product_image):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()

    try:
        # Insert the product into the database
        cursor.execute(
            "INSERT INTO Products (product_name, product_price, product_weight, product_image) "
            "VALUES (?, ?, ?, ?)",
            (product_name, product_price, product_weight, product_image)
        )

        dbconnect.commit()
        return True
    except Exception as e:
        # Handle any exceptions that occur during the insertion
        print(f"Error inserting product into database: {str(e)}")
        dbconnect.rollback()
        return False
    finally:
        cursor.close()


def delete_product(product_id):

    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()

    cursor.execute(f"DELETE FROM Products WHERE product_ID = {product_id}")
    cursor.commit()
    cursor.close()



def insert(fname, lname, email, newpassword, number, address):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    hashed_password = bcrypt.hashpw(newpassword.encode(),bcrypt.gensalt()).decode()
    cursor.execute(
        f"Insert into Customers(first_name,last_name,email_address,password,contact_no,address,role) VALUES('{fname}', '{lname}', '{email}','{hashed_password}','{number}' ,'{address}','1')")
    cursor.commit()
    cursor.close()
    return 'Added User'
def check_email_exists(email):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute(f"SELECT * FROM Customers WHERE email_address='{email}'")
    row = cursor.fetchone()
    cursor.close()
    return row
def retrieve(username, newpassword):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute(f"SELECT password FROM Customers WHERE email_address = '{username}'")
    row = cursor.fetchone()
    hashed_password = row[0]

    if bcrypt.checkpw(newpassword.encode('utf-8'),hashed_password.encode('utf-8')):
        return True
    else:
        return False




def retrieveadmin(username, newpassword):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute(
        f"SELECT * FROM Admin WHERE email_address = '{username}' AND password = '{newpassword}' AND role = '2'")
    row = cursor.fetchall()
    return row


def get_products():
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute("SELECT product_ID, product_name,product_image, product_price, product_weight FROM Products")
    rows = cursor.fetchall()
    Product = namedtuple('Product', [column[0] for column in cursor.description])
    return [dict(Product._make(row)._asdict()) for row in rows]


# def add_to_cart(product_ID, quantity):
#     dbconnect = pyodbc.connect(connection)
#     cursor = dbconnect.cursor()
#
#     # Check if the product already exists in the cart
#     cursor.execute("SELECT quantity FROM Cart WHERE product_id = ?", (product_ID,))
#     row = cursor.fetchone()
#
#     if row is None:
#         # Product does not exist in the cart, add it with the specified quantity
#         cursor.execute("INSERT INTO Cart (product_id, quantity) VALUES (?, ?)", (product_ID, quantity))
#     else:
#         # Product already exists in the cart, update the quantity
#         cursor.execute("UPDATE Cart SET quantity = quantity + ? WHERE product_id = ?", (quantity, product_ID))
#
#     cursor.commit()
#     cursor.close()
#
#     return jsonify({'message': 'Item added to cart'})
def add_to_cart(product_ID, quantity, customer_email):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()

    # Retrieve the customer ID based on the email
    cursor.execute("SELECT customer_ID FROM Customers WHERE email_address = ?", (customer_email,))
    row = cursor.fetchone()
    if row:
        customer_id = row[0]

        # Check if the product already exists in the cart for the customer
        cursor.execute("SELECT quantity FROM Cart WHERE customer_ID = ? AND product_id = ?", (customer_id, product_ID))
        row = cursor.fetchone()

        if row is None:
            # Product does not exist in the cart, add it with the specified quantity
            cursor.execute("INSERT INTO Cart (customer_ID, product_id, quantity) VALUES (?, ?, ?)", (customer_id, product_ID, quantity))
        else:
            # Product already exists in the cart, update the quantity
            new_quantity = row.quantity + quantity
            cursor.execute("UPDATE Cart SET quantity = ? WHERE customer_ID = ? AND product_id = ?", (new_quantity, customer_id, product_ID))

        cursor.commit()
        cursor.close()

        return {'status': 'success', 'message': 'Item added to cart'}
    else:
        return {'status': 'error', 'message': 'Customer not found'}





def get_cart(customer_email):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute("""
        SELECT Products.product_name, Products.product_price, SUM(Cart.quantity) as quantity, Products.product_ID
        FROM Cart
        INNER JOIN Products ON Cart.product_ID = Products.product_ID
        INNER JOIN Customers ON Cart.customer_ID = Customers.customer_ID
        WHERE Customers.email_address = ?
        GROUP BY Products.product_name, Products.product_price, Products.product_ID
        """, (customer_email,))
    cart_items = cursor.fetchall()
    Items = namedtuple('CartItem', [column[0] for column in cursor.description])
    items_dict = [dict(Items._make(row)._asdict()) for row in cart_items]
    cursor.close()
    return items_dict



def remove_from_cart(customer_id, product_ID):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()
    cursor.execute("SELECT quantity FROM Cart WHERE customer_ID = ? AND product_ID = ?", (customer_id, product_ID))
    row = cursor.fetchone()
    if row:
        if row[0] > 1:
            new_quantity = row[0] - 1
            cursor.execute("UPDATE Cart SET quantity = ? WHERE customer_ID = ? AND product_ID = ?", (new_quantity, customer_id, product_ID))
        else:
            cursor.execute("DELETE FROM Cart WHERE customer_ID = ? AND product_ID = ?", (customer_id, product_ID))
        dbconnect.commit()
        cursor.close()
        return {'status': 'success', 'message': 'Item removed from cart'}
    else:
        return {'status': 'error', 'message': 'Item not found in cart'}

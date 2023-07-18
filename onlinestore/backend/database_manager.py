
from collections import namedtuple
from datetime import date

import pyodbc
import bcrypt



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

    try:
        # Check if the product exists in any cart
        cursor.execute("SELECT cart_id FROM CartItems WHERE product_id = ?", (product_id,))
        rows = cursor.fetchall()

        if rows:
            # Delete the items associated with the product from the CartItems table
            cursor.execute("DELETE FROM CartItems WHERE product_id = ?", (product_id,))
            dbconnect.commit()

        # Delete the product from the Products table
        cursor.execute("DELETE FROM Products WHERE product_ID = ?", (product_id,))
        dbconnect.commit()

        return {'status': 'success', 'message': 'Product deleted successfully'}
    except Exception as e:
        # Handle any exceptions that occur during the deletion
        print(f"Error deleting product from database: {str(e)}")
        dbconnect.rollback()
        return {'status': 'error', 'message': 'Failed to delete product. Check the database connection and try again.'}
    finally:
        cursor.close()



def edit_product(product_id, product_name, product_price, product_weight, product_image):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()

    try:
        # Update the product in the database
        cursor.execute(
            "UPDATE Products SET product_name = ?, product_price = ?, product_weight = ?, product_image = ? "
            "WHERE product_ID = ?",
            (product_name, product_price, product_weight, product_image, product_id)
        )

        dbconnect.commit()
        return True
    except Exception as e:
        # Handle any exceptions that occur during the update
        print(f"Error updating product in the database: {str(e)}")
        dbconnect.rollback()
        return False
    finally:
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

# Function to create an order in the database
def create_order(user, total_amount):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()

    # Retrieve the customer ID based on the email address
    cursor.execute(f"SELECT customer_id FROM Customers WHERE email_address = '{user}'")
    customer_id = cursor.fetchone()[0]

    # Insert the order into the Orders table
    current_date = date.today().strftime("%Y-%m-%d")
    cursor.execute(
        f"INSERT INTO Orders (customer_id, total_amount, order_date) VALUES ({customer_id}, {total_amount}, '{current_date}')")
    cursor.commit()

    # Retrieve the generated order ID
    order_id = cursor.execute("SELECT SCOPE_IDENTITY()").fetchone()[0]

    cursor.close()
    return order_id

# Function to add an order item to the order
def add_order_item(order_id, product_id, quantity, product_price):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()

    cursor.execute(
        "INSERT INTO OrderItems (order_id, product_id, quantity, unit_price) "
        f"VALUES ({order_id}, {product_id}, {quantity}, {product_price})"
    )
    cursor.commit()

    cursor.close()

# Function to clear the user's cart
def clear_cart(user):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()

    # Retrieve the customer ID based on the email address
    cursor.execute("SELECT customer_ID FROM Customers WHERE email_address = ?", (user,))
    row = cursor.fetchone()
    if row:
        customer_id = row[0]

        # Delete the cart items associated with the customer
        cursor.execute("DELETE FROM CartItems WHERE cart_id IN (SELECT cart_id FROM Cart WHERE customer_id = ?)",
                       (customer_id,))

        # Delete the cart
        cursor.execute("DELETE FROM Cart WHERE customer_id = ?", (customer_id,))
        cursor.commit()

        cursor.close()

        return {'message': 'Cart cleared successfully'}
    else:
        cursor.close()
        return {'error': 'Customer not found'}


def add_to_cart(product_ID, quantity, customer_email):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()

    # Retrieve the customer ID based on the email
    cursor.execute("SELECT customer_ID FROM Customers WHERE email_address = ?", (customer_email,))
    row = cursor.fetchone()
    if row:
        customer_id = row[0]

        # Check if the product already exists in the cart for the customer
        cursor.execute("SELECT cart_id FROM Cart WHERE customer_ID = ?", (customer_id,))
        row = cursor.fetchone()

        if row:
            cart_id = row[0]
        else:
            # Create a new cart for the customer
            cursor.execute("INSERT INTO Cart (customer_ID) VALUES (?)", (customer_id,))
            dbconnect.commit()

            # Retrieve the newly generated cart_id using SCOPE_IDENTITY()
            cursor.execute("SELECT SCOPE_IDENTITY()")
            cart_id = cursor.fetchone()[0]

        # Insert the product into the CartItems table
        cursor.execute("INSERT INTO CartItems (cart_id, product_id, quantity) VALUES (?, ?, ?)",
                       (cart_id, product_ID, quantity))

        # Calculate the current total of the cart
        cursor.execute(
            """
            SELECT SUM(P.product_price * CI.quantity)
            FROM CartItems CI
            INNER JOIN Products P ON CI.product_ID = P.product_ID
            WHERE CI.cart_id = ?
            """,
            (cart_id,)
        )
        total = cursor.fetchone()[0] or 0  # Get the sum or default to 0 if no items in cart

        # Update the total value in the Cart table
        cursor.execute("UPDATE Cart SET total = ? WHERE cart_id = ?", (total, cart_id))

        dbconnect.commit()
        cursor.close()

        return {'status': 'success', 'message': 'Item added to cart'}
    else:
        return {'status': 'error', 'message': 'Customer not found'}



def remove_from_cart(customer_email, product_ID):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()

    # Retrieve the customer ID based on the email
    cursor.execute("SELECT customer_ID FROM Customers WHERE email_address = ?", (customer_email,))
    row = cursor.fetchone()
    if row:
        customer_id = row[0]

        # Retrieve the cart ID for the customer
        cursor.execute("SELECT cart_id FROM Cart WHERE customer_id = ?", (customer_id,))
        row = cursor.fetchone()
        if row:
            cart_id = row[0]

            # Check if the product exists in the cart
            cursor.execute(
                "SELECT quantity FROM CartItems WHERE cart_id = ? AND product_id = ?",
                (cart_id, product_ID)
            )
            row = cursor.fetchone()

            if row:
                if row[0] > 1:
                    new_quantity = row[0] - 1
                    cursor.execute(
                        "UPDATE CartItems SET quantity = ? WHERE cart_id = ? AND product_id = ?",
                        (new_quantity, cart_id, product_ID)
                    )
                else:
                    cursor.execute(
                        "DELETE FROM CartItems WHERE cart_id = ? AND product_id = ?",
                        (cart_id, product_ID)
                    )

                # Calculate the current total of the cart
                cursor.execute(
                    """
                    SELECT SUM(P.product_price * CI.quantity)
                    FROM CartItems CI
                    INNER JOIN Products P ON CI.product_ID = P.product_ID
                    WHERE CI.cart_id = ?
                    """,
                    (cart_id,)
                )
                total = cursor.fetchone()[0] or 0  # Get the sum or default to 0 if no items in cart

                # Update the total value in the Cart table
                cursor.execute("UPDATE Cart SET total = ? WHERE cart_id = ?", (total, cart_id))

                dbconnect.commit()
                cursor.close()
                return {'status': 'success', 'message': 'Item removed from cart'}
            else:
                return {'status': 'error', 'message': 'Item not found in cart'}

    # No customer or cart found
    cursor.close()
    return {'status': 'error', 'message': 'Customer not found or cart is empty'}


def get_cart(customer_email):
    dbconnect = pyodbc.connect(connection)
    cursor = dbconnect.cursor()

    # Retrieve the customer ID based on the email
    cursor.execute("SELECT customer_ID FROM Customers WHERE email_address = ?", (customer_email,))
    row = cursor.fetchone()
    if row:
        customer_id = row[0]

        # Retrieve the cart ID for the customer
        cursor.execute("SELECT cart_id FROM Cart WHERE customer_id = ?", (customer_id,))
        row = cursor.fetchone()
        if row:
            cart_id = row[0]

            # Retrieve the cart items
            cursor.execute("""
                SELECT P.product_name, P.product_price, CI.quantity, P.product_ID
                FROM CartItems CI
                INNER JOIN Products P ON CI.product_ID = P.product_ID
                WHERE CI.cart_id = ?
                """, (cart_id,))
            cart_items = cursor.fetchall()
            Items = namedtuple('CartItems', [column[0] for column in cursor.description])
            items_dict = [dict(Items._make(row)._asdict()) for row in cart_items]
            cursor.close()
            return items_dict

    # No customer or cart found
    cursor.close()
    return {'status': 'error', 'message': 'Customer not found or cart is empty'}







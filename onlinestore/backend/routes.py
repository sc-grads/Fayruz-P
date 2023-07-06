import json
from flask import Flask, request, jsonify
from functools import wraps

import database_manager as dbm
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'])
app.secret_key = 'abcd'

local_session = {}

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'user' not in local_session:
#             return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401
#         return f(*args, **kwargs)
#     return decorated_function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in local_session:
            return jsonify({'status': 'error', 'message': 'Unauthorized:Please log in'}), 401
        return f(*args, **kwargs)
    return decorated_function
@app.route('/check_session_status')
def check_session_status():

    if 'user' in local_session:
        return jsonify(True)
    else:
        return jsonify(False)

@app.route('/checkadminlogin')
def check_admin_login():
    if 'user' in local_session and local_session['role'] == 'admin':
        return jsonify({'status': 'success', 'message': 'Admin logged in'})
    elif 'user' not in local_session:
        return jsonify({'status': 'error', 'message': 'Unauthorized: Please log in as admin'}), 401
    else:
        return jsonify({'status': 'error', 'message': 'Admin privileges required'}), 403


@app.route('/product/<int:product_id>', methods=['PUT'])
@login_required
def edit_product(product_id):
    # Extract the updated product information from the request data
    product_data = request.get_json()
    product_name = product_data['product_name']
    product_price = product_data['product_price']
    product_weight = product_data['product_weight']
    product_image = product_data['product_image']

    # Update the product in the database
    success = dbm.edit_product(product_id, product_name, product_price, product_weight, product_image)

    if success:
        return jsonify({'status': 'success', 'message': 'Product updated successfully'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Failed to update product. Check the database connection and verify the data.'}), 500

@app.route('/product', methods=['POST'])
@login_required
def add_product():
    # Extract the product information from the request data
    product_data = request.get_json()
    product_name = product_data['product_name']
    product_price = product_data['product_price']
    product_weight = product_data['product_weight']
    product_image = product_data['product_image']

    # Insert the product into the database
    success = dbm.insert_product(product_name, product_price, product_weight, product_image)

    if success:
        return jsonify({'status': 'success', 'message': 'Product added successfully'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Failed to add product.'}), 500

@app.route('/product/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product_route(product_id):
    dbm.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
    # Extract the user credentials from the request data
    userdata = request.get_json()
    username = userdata['username']
    password = userdata['password']

    # Authenticate the user
    user = dbm.retrieve(username, password)
    local_session['user'] = username
    local_session['role'] = 'customer'
    print(local_session)

    if not username or not password:
        return jsonify({'status': 'error', 'message': 'Please fill in all required fields'})

    if user:
        return jsonify({'status': 'success', 'message': 'Login Successful'})
    else:
        return jsonify({'status': 'error', 'message': 'Login Unsuccessful'})

@app.route('/register', methods=['POST'])
def register():
    # Extract the user registration data from the request
    registerinfo = request.json
    fname = registerinfo.get('fname')
    lname = registerinfo.get('lname')
    email = registerinfo.get('email')
    password = registerinfo.get('password')
    number = registerinfo.get('number')
    address = registerinfo.get('address')

    # Validate email and password fields
    if not fname or not lname or not email or not password or not number or not address:
        return jsonify({'status': 'error', 'message': 'Please fill in all required fields'})

    # Check if email already exists
    row = dbm.check_email_exists(email)
    if row:
        return jsonify({'status': 'error', 'message': 'Email already exists'})

    # Insert new user
    dbm.insert(fname, lname, email, password, number, address)
    return jsonify({'status': 'success', 'message': 'Registration successful'})

@app.route('/logout', methods=['POST'])
def logout():
    local_session.pop('user', None)
    local_session.pop('role', None)
    print(local_session)
    return jsonify({'status': 'success', 'message': 'Logout Successful'})

@app.route('/dashboard')
def dashboard():
    return jsonify({'status': 'Success'}), 200

@app.route('/adminlogin', methods=['POST'])
def adminlogin():
    # Extract the admin credentials from the request data
    admindata = request.get_json()
    adminusername = admindata['username']
    adminpassword = admindata['password']

    # Authenticate the admin
    dbm.retrieveadmin(adminusername, adminpassword)
    local_session['user'] = adminusername
    local_session['role'] = 'admin'
    print(local_session)

    if not adminusername or not adminpassword:
        return jsonify({'status': 'error', 'message': 'Please fill in all required fields'})

    if dbm.retrieveadmin(adminusername, adminpassword):
        return jsonify({'status': 'success', 'message': 'Login Successful'})
    else:
        return jsonify({'status': 'error', 'message': 'Login Unsuccessful'})

@app.route('/admindashboard')
def admin_dashboard():
    return jsonify({'status': 'Success'}), 200

@app.route('/cart')
def cart_retrieve():
    user = local_session.get('user')
    if user:
        items = dbm.get_cart(user)
        print(f"Session created for user {user}")
        return jsonify(items), 200
    else:
        return jsonify({'status': 'error', 'message': 'Please log in to access the cart'})

@app.route('/add_to_cart', methods=['POST'])
def cart_add():
    user = local_session.get('user')
    if user:
        data = request.json
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        dbm.add_to_cart(product_id, quantity, user)
        return jsonify({'status': 'success', 'message': 'Item added to cart'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Please log in to add items to the cart'})

@app.route('/remove_from_cart/<int:product_id>', methods=['DELETE'])
def cart_remove(product_id):
    user = local_session.get('user')
    if user:
        dbm.remove_from_cart(user, product_id)
        if len(dbm.get_cart(user)) > 0:
            return jsonify({'status': 'success', 'message': 'Cart refreshed'}), 200
        else:
            return jsonify({'status': 'success', 'message': 'Item removed from cart'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Please log in to remove items from the cart'})

@app.route('/favicon.ico')
def favicon():
    return '', 200

@app.route('/shop', methods=['GET'])
def products_retrieve():
    products = dbm.get_products()
    return jsonify(products), 200


@app.route('/checkout', methods=['POST'])
def checkout():
    user = local_session.get('user')
    if user:
        # Retrieve cart items for the user
        items = dbm.get_cart(user)

        # Calculate total amount
        total_amount = sum(item['product_price'] * item['quantity'] for item in items)

        # Create an order in the database
        order_id = dbm.create_order(user, total_amount)
        # Retrieve cart items for the user
        cart_items = dbm.get_cart(user)

        # Create a list of items with the required keys
        items = []
        for cart_item in cart_items:
            item = {
                'product_ID': cart_item['product_ID'],
                'quantity': cart_item['quantity'],
                'product_price': cart_item['product_price']
            }
            items.append(item)

        # Add order items to the order
        for item in items:
            dbm.add_order_item(order_id, item['product_ID'], item['quantity'], item['product_price'])

        # Clear the user's cart
        dbm.clear_cart(user)

        return {'message': 'Order placed successfully'}
    else:
        return {'error': 'User not authenticated'}

if __name__ == '__main__':
    app.run(debug=True)

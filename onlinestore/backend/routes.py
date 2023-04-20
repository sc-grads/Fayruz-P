import json
from collections import namedtuple
from flask import Flask, request, jsonify
import database_manager as dbm
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'])
app.secret_key = 'abcd'

local_session = {}



@app.route('/login', methods=['POST'])
def login():
    userdata = request.get_json()
    username = userdata['username']
    password = userdata['password']
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

    return jsonify({'status': 'User Logged in as Customer'}), 200



@app.route('/register', methods=['POST', 'GET'])
def register():
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
    admindata = request.get_json()
    adminusername = admindata['username']
    adminpassword = admindata['password']
    dbm.retrieveadmin(adminusername, adminpassword)
    local_session['user'] = adminusername
    local_session['role'] = 'admin'
    print(local_session)
    if not adminusername or not adminpassword:
        return jsonify({'status': 'error', 'message': 'Please fill in all required fields'})

    dbm.retrieveadmin(adminusername, adminpassword)
    if dbm.retrieveadmin(adminusername, adminpassword):
        return jsonify({'status': 'success', 'message': 'Login Successful'})
    else:
        return jsonify({'status': 'error', 'message': 'Login Unsuccessful'})

    return jsonify({'status': 'User Logged in as Customer'}), 200







@app.route('/admindashboard')
def admin_dashboard():
    return jsonify({'status': 'Success'}), 200


@app.route('/cart')
def cart_retrieve():
    items = dbm.get_cart()
    user = local_session.get('user')
    print(f"Session created for user {user}")
    return jsonify(items), 200


@app.route('/add_to_cart', methods=['POST'])
def cart_add():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    dbm.add_to_cart(product_id, quantity)
    return jsonify({'status': 'Added to cart'}), 200


@app.route('/remove_from_cart/<int:product_id>', methods=['DELETE'])
def cart_remove(product_id):
    dbm.remove_from_cart(product_id)
    if len(dbm.get_cart()) > 0:
        dbm.get_cart()
        return jsonify({'status': 'Cart refreshed'}), 200
    else:
        return jsonify({'status': 'Removed from cart'}), 200


@app.route('/favicon.ico')
def favicon():
    return '', 200


@app.route('/shop', methods=['GET'])
def products_retrieve():
    products = dbm.get_products()
    return jsonify(products), 200


if __name__ == '__main__':
    app.run(debug=True)

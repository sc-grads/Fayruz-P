import json
from collections import namedtuple
from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
import database_manager as dbm

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'])


# app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SECRET_KEY'] = 'AbY&FaY1008'
# Session(app)
# @app.route('/set-customer-profile', methods=['POST'])
# def set_customer_profile():
#     data = request.get_json()
#     session['customer_profile'] = data
#     return 'Customer profile set.'
#
#
# @app.route('/get-customer-profile', methods=['GET'])
# def get_customer_profile():
#     return session.get('customer_profile', {})


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    dbm.retrieve(username, password)
    return {'Status': 'User Logged in'}


@app.route('/register', methods=['GET', 'POST'])
def register():
    registerinfo = request.json
    fname = registerinfo.get('fname')
    lname = registerinfo.get('lname')
    email = registerinfo.get('email')
    password = registerinfo.get('password')
    number = registerinfo.get('number')
    address = registerinfo.get('address')
    dbm.insert(fname, lname, email, password, number, address)
    return {'200': 'User Registered and Redirected'}


@app.route('/dashboard')
def dashboard():
    return {'Status': 'Success'}


@app.route('/cart')
def cart_retrieve():
    dbm.get_cart()
    return {'200': 'Cart Retrieved!'}


@app.route('/add_to_cart', methods=['POST'])
def cart_add():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    dbm.add_to_cart(product_id, quantity)
    return {'200': 'Added to cart'}


@app.route('/favicon.ico')
def favicon():
    return ''



@app.route('/shop', methods=['GET'])
def products_retrieve():
    products = dbm.get_products()
    return products





if __name__ == '__main__':
    app.run(debug=True)

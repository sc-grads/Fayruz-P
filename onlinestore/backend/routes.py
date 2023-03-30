
import json
from collections import namedtuple
from flask import Flask, request, redirect, jsonify
=======
from flask import Flask, request, redirect


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

=======
@app.route('/dashboard')
def dashboard():
    return None





if __name__ == '__main__':
    app.run(debug=True)

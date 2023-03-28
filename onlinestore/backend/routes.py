from flask import Flask, request, redirect
from flask_cors import CORS
from pip._internal.network import session

import database_manager as dbm
from flask_session import Session

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'])
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'AbY&FaY1008'
Session(app)
@app.route('/set-customer-profile', methods=['POST'])
def set_customer_profile():
    data = request.get_json()
    session['customer_profile'] = data
    return 'Customer profile set.'

@app.route('/get-customer-profile', methods=['GET'])
def get_customer_profile():
    return session.get('customer_profile', {})

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
    return None




if __name__ == '__main__':
    app.run(debug=True)

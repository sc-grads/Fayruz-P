from flask import Flask, request
from flask_cors import CORS
import database_manager as dbm

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'])


@app.route('/login', methods=['POST'])
def login():
    userinfo = request.json
    user = userinfo.get('username')
    password = userinfo.get('password')
    print(user)
    print(password)
    isconnected = dbm.conn()
    return {'Status': isconnected}


@app.route('/register', methods=['POST'])
def register():
    registerinfo = request.json
    fname = registerinfo.get('fname')
    lname = registerinfo.get('lname')
    email = registerinfo.get('email')
    password = registerinfo.get('password')
    number = registerinfo.get('number')
    address = registerinfo.get('address')
    dbm.insert(fname,lname,email,password,number,address)
    return {'Status': 'User Registered'}



if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request
from flask_cors import CORS
import database_manager as dbm


app = Flask(__name__)
CORS(app,origins=['http://localhost:4200'])


@app.route('/login', methods=['POST'])
def login():
    userinfo = request.json
    user = userinfo.get('username')
    password = userinfo.get('password')
    print(user)
    print(password)
    isconnected = dbm.conn()
    return{'Status': isconnected}

@app.route('/register', methods=['POST'])
def register():
    registerinfo = request.json
    fname = registerinfo.get('firstname')
    lname = registerinfo.get('lastname')
    user = registerinfo.get('username')
    email = registerinfo.get('email')
    password = registerinfo.get('password')
    number = registerinfo.get('contactnumber')
    address = registerinfo.get('address')



if __name__ == '__main__':
    app.run(debug=True)

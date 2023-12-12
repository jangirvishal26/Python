import requests
from flask import Flask, request

app = Flask(__name__)

def login():
    # Combining source and sink in the same function
    username = request.args.get('username')
    password = request.args.get('password')

    # Processing the input (sink)
    if username == "admin" and password == "secretpassword":
        return "Login successful"
    else:
        return "Login failed"

# Example Flask route using the login function
@app.route('/login')
def login_route():
    return login()

if __name__ == '__main__':
    app.run(debug=True)

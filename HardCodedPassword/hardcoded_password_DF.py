import requests


USERNAME = "admin"
PASSWORD = "secretpassword"
text = "Hello"
def authenticate(username, password):
    if username == USERNAME and password == PASSWORD:
        return True
    else:
        return False

def login(request):
    username = request.args.get('username')
    password = request.args.get('password')

    if authenticate(username, password):
        return "Login successful"
    else:
        return "Login failed"

# Example Flask route using the login function
from flask import Flask, request

app = Flask(__name__)

@app.route('/login')
def login_route():
    return login(request)

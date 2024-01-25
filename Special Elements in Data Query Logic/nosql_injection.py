from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['example_db']

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    # Vulnerable code - directly incorporating user input into MongoDB query
    user_data = db.users.find_one({'username': username, 'password': password})

    if user_data:
        return "Login successful"
    else:
        return "Login failed"

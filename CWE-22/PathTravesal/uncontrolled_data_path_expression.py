import os.path
from flask import Flask, request, abort

app = Flask(__name__)

def read_picture_from_path(path):
    data = open(path, 'rb').read()
    return data

def validate_path(base_path, full_path):
    full_path = os.path.normpath(full_path)
    if not full_path.startswith(base_path):
        raise Exception("Not allowed")

def user_picture1():
    filename = request.args.get('p')
    data = read_picture_from_path(filename)
    return data

def user_picture2():
    base_path = '/server/static/images'
    filename = request.args.get('p')
    full_path = os.path.join(base_path, filename)
    validate_path(base_path, full_path)
    data = read_picture_from_path(full_path)
    return data

def user_picture3():
    base_path = '/server/static/images'
    filename = request.args.get('p')
    full_path = os.path.join(base_path, filename)
    validate_path(base_path, full_path)
    data = read_picture_from_path(full_path)
    return data

# Route mappings
app.route("/user_picture1")(user_picture1)
app.route("/user_picture2")(user_picture2)
app.route("/user_picture3")(user_picture3)

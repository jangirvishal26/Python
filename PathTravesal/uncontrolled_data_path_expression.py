import os.path
from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/user_picture1")
def user_picture1():
    filename = request.args.get('p')
    data = open(filename, 'rb').read()
    return data

@app.route("/user_picture2")
def user_picture2():
    base_path = '/server/static/images'
    filename = request.args.get('p')
    data = open(os.path.join(base_path, filename), 'rb').read()
    return data

@app.route("/user_picture3")
def user_picture3():
    base_path = '/server/static/images'
    filename = request.args.get('p')
    fullpath = os.path.normpath(os.path.join(base_path, filename))
    if not fullpath.startswith(base_path):
        raise Exception("not allowed")
    data = open(fullpath, 'rb').read()
    return data

from flask import Flask
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Secret info")

def handle_exception_bad():
    return traceback.format_exc()

def handle_exception_good():
    log(traceback.format_exc())
    return "An internal error has occurred!"

# BAD
@app.route('/bad')
def server_bad():
    try:
        do_computation()
    except Exception as e:
        return handle_exception_bad()

# GOOD
@app.route('/good')
def server_good():
    try:
        do_computation()
    except Exception as e:
        return handle_exception_good()

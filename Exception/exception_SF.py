from flask import Flask
import traceback

app = Flask(__name__)

# BAD
@app.route('/bad')
def server_bad():
    try:
        # Combining source and sink in the same function
        raise Exception(request.args.get('input', ''))
    except Exception as e:
        return traceback.format_exc()

# GOOD
@app.route('/good')
def server_good():
    try:
        # Combining source and sink in the same function
        log(request.args.get('input', ''))
        raise Exception("An internal error has occurred!")
    except Exception as e:
        return traceback.format_exc()

def log(data):
    # Dummy log function
    print("Logging:", data)

from flask import Flask, request, make_response, escape

app = Flask(__name__)

def get_unsafe_input():
    return request.args.get('name', '')

def render_unsafe_response(input_data):
    return make_response("Your name is " + input_data)

@app.route('/unsafe')
def unsafe():
    input_data = get_unsafe_input()
    return render_unsafe_response(input_data)

def get_safe_input():
    return request.args.get('name', '')

def render_safe_response(input_data):
    return make_response("Your name is " + escape(input_data))

@app.route('/safe')
def safe():
    input_data = get_safe_input()
    return render_safe_response(input_data)

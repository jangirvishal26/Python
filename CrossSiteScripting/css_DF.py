from flask import Flask, request, make_response, escape

app = Flask(__name__)

def get_user_input():
    # Method to retrieve user input, assuming 'name' is a query parameter
    return request.args.get('name', '')

def construct_response(user_input):
    # Method to construct the response, escaping the user input
    return "Your name is " + user_input

@app.route('/unsafe')
def unsafe():
    first_name = get_user_input()
    response_content = construct_response(first_name)
    return make_response(response_content)

@app.route('/safe')
def safe():
    first_name = get_user_input()
    # Use escape to mitigate potential HTML injection attacks
    response_content = construct_response(escape(first_name))
    return make_response(response_content)

from flask import Flask, request
import re

app = Flask(__name__)

def get_user_input():
    return request.args['regex'], request.args['data']

def perform_regex_search(regex, data):
    re.search(regex, data)

@app.route('/lookup')
def lookup():
    regex, data = get_user_input()
    perform_regex_search(regex, data)
    

import requests
from flask import Flask, request, render_template

app = Flask(__name__)

def get_user_input():
    # Source: Obtaining user input
    return request.args.get('url', '')

def make_request(url):
    # Sink: Making an HTTP request using user input
    try:
        response = requests.get(url)
        return f"Response: {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch')
def fetch_url():
    url = get_user_input()
    return make_request(url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

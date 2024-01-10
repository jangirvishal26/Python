from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('username', '')
    response = make_response(f'Hello, {username}!')
    
    # Attacker-controlled input in the User-Agent header
    user_agent = request.headers.get('User-Agent', '')
    response.headers['User-Agent'] = user_agent

    return response

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, make_response, escape

app = Flask(__name__)

def get_user_input():
    username = request.args.get('username', '')
    return username

def set_user_agent_header(response, user_agent):
    response.headers['User-Agent'] = user_agent

@app.route('/login')
def login():
    username = get_user_input()
    
    # Attacker-controlled input in the User-Agent header
    user_agent = request.headers.get('User-Agent', '')

    response = make_response(f'Hello, {username}!')
    set_user_agent_header(response, user_agent)

    return response

if __name__ == '__main__':
    app.run(debug=True)

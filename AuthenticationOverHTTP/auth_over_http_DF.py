from flask import Flask, request, jsonify

app = Flask(__name__)

def get_credentials():
    username = request.form.get('username')
    password = request.form.get('password')
    return username, password

def authenticate(username, password):
    if username == 'admin' and password == 'password':
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'})

@app.route('/login', methods=['POST'])
def login():
    username, password = get_credentials()
    return authenticate(username, password)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

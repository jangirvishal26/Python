from flask import Flask, request, jsonify

app = Flask(__name__)

# Insecure authentication over HTTP
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'admin' and password == 'password':
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

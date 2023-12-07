from flask import Flask, request, abort

app = Flask(__name__)

# Mocked user database
users = {
    'alice': {'password': 'password123', 'role': 'user'},
    'bob': {'password': 'securepass', 'role': 'admin'},
}

def access_sensitive_data():
    username = request.args.get('username')
    password = request.args.get('password')

    user = users.get(username)

    if user and user['password'] == password:
        role = user['role']
        if role == 'admin':
            return "You have access to sensitive data!"
        else:
            abort(403, "Access forbidden. Insufficient permissions.")
    else:
        abort(401, "Unauthorized. Invalid credentials.")

# Route for accessing sensitive data
@app.route('/sensitive-data')
def sensitive_data_route():
    # BAD: Combining input retrieval and processing
    return access_sensitive_data()

if __name__ == '__main__':
    app.run(debug=True)

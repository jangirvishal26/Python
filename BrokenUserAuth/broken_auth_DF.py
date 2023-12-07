from flask import Flask, request, abort

app = Flask(__name__)

# Mocked user database
users = {
    'alice': {'password': 'password123', 'role': 'user'},
    'bob': {'password': 'securepass', 'role': 'admin'},
}

def authenticate(username, password):
    user = users.get(username)
    if user and user['password'] == password:
        return user
    else:
        return None

def get_user_role(request):
    username = request.args.get('username')
    password = request.args.get('password')
    
    user = authenticate(username, password)

    if user:
        return user['role']
    else:
        return "Invalid credentials"

# Route for accessing sensitive data
@app.route('/sensitive-data')
def sensitive_data_route():
    # BAD: Broken User Authentication
    role = get_user_role(request)
    
    if role == 'admin':
        return "You have access to sensitive data!"
    else:
        abort(403, "Access forbidden. Insufficient permissions.")

if __name__ == '__main__':
    app.run(debug=True)

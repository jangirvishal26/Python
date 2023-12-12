from flask import Flask, request, redirect

app = Flask(__name__)

# Dummy user data (for demonstration purposes)
users = {'admin': 'admin_password', 'user1': 'password1', 'user2': 'password2'}

# Route for handling login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Simulate authentication (plain text passwords for demonstration purposes)
    if username in users and users[username] == password:
        return f'Welcome, {username}!'
    else:
        return 'Invalid username or password.'

# Route for an admin-only resource
@app.route('/admin/dashboard')
def admin_dashboard():
    username = request.args.get('username')

    # Simulate an authorization check (insecure implementation)
    if username == 'admin':
        return 'Admin dashboard content.'
    else:
        return 'Unauthorized access.'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, session, redirect

app = Flask(__name__)

# initiate the session in order to validate sessions
app.secret_key = 'your_secret_key'

# If the session is registered to a valid user, then allow update
@app.route('/update_profile', methods=['POST'])
def update_profile():
    # Check if the session is registered to a valid user
    if 'username' not in session:
        return "Invalid session detected! Redirect user to login page..."

    # The user session is valid, so process the request and update the information
    username = session['username']
    email = request.form.get('email')
    
    # Send an update to the database (replace this with your actual database update logic)
    send_update_to_database(username, email)

    return "Your profile has been successfully updated."

# Function to simulate sending an update to the database
def send_update_to_database(username, email):
    # Replace this with your actual database update logic
    print(f"Updating database for user {username} with email {email}")

if __name__ == '__main__':
    app.run(debug=True)

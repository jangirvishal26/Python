from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Assume 'session_token' is a sensitive cookie containing user session information
    session_token = request.cookies.get('session_token')

    # Process user session based on the cookie
    if session_token:
        # Do something with the session_token, like checking user authentication
        authenticated = check_authentication(session_token)

        if authenticated:
            return "Welcome to the secure area!"
        else:
            return "Unauthorized access!"
    else:
        return "Please log in to access this page."

def check_authentication(session_token):
    # Simulated authentication check
    # In a real application, this would involve validating the session_token
    # against a user database or some authentication mechanism
    # For the purpose of this example, we'll just assume the token is valid
    return True

if __name__ == '__main__':
    app.run(debug=True)

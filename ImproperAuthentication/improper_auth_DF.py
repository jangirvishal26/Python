class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, username):
        # Generate a session token (insecurely for the purpose of this example)
        session_token = f"{username}_insecure_token"
        self.sessions[session_token] = username
        return session_token

    def authenticate_user(self, session_token):
        # Check if the session token is valid
        return session_token in self.sessions

    def get_username(self, session_token):
        # Get the username associated with the session token
        return self.sessions.get(session_token)

def process_request(session_manager, session_token):
    # Check if the session token is valid
    if session_manager.authenticate_user(session_token):
        # Get the username associated with the session token
        username = session_manager.get_username(session_token)

        # Check if the user has administrator privileges
        if username == "Administrator":
            print("Administrator tasks performed.")
        else:
            print("Regular user tasks performed.")
    else:
        print("Error: Authentication failed.")

# Attacker manipulating the session token
attacker_session_token = "Administrator_insecure_token"

# Simulate processing the request with the manipulated session token
session_manager = SessionManager()
process_request(session_manager, attacker_session_token)

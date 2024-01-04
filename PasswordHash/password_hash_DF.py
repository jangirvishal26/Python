import hashlib

def source_password_hash(password):
    # Source method: Insecure use of the MD5 hash function
    return hashlib.md5(password.encode()).hexdigest()

def verify_password(incoming_password_hash, stored_hashed_password):
    # Verify the password by comparing the stored hash with the hash of the incoming password hash
    return incoming_password_hash == stored_hashed_password

# Example usage (insecure)
user_password = "my_secure_password"

# Source: Obtain the hash of the user's password
incoming_password_hash = source_password_hash(user_password)

# Sink: Simulate a login attempt
stored_hashed_password = incoming_password_hash
incoming_password_attempt_hash = "attacker_attempting_to_guess_password"

login_successful = verify_password(incoming_password_attempt_hash, stored_hashed_password)

if login_successful:
    print("Login successful")
else:
    print("Login failed")

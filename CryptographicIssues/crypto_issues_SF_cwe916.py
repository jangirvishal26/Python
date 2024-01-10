import hashlib

def insecure_hash_password(password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password

def verify_password(incoming_password, stored_hashed_password):
    return insecure_hash_password(incoming_password) == stored_hashed_password


user_password = "my_secure_password"
stored_hashed_password = insecure_hash_password(user_password)

# Simulate a login attempt
incoming_password_attempt = "attacker_attempting_to_guess_password"
login_successful = verify_password(incoming_password_attempt, stored_hashed_password)

if login_successful:
    print("Login successful")
else:
    print("Login failed")

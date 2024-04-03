import hashlib
import random

def generate_insecure_token(username):
    # WARNING: Insecure use of the random module for token generation
    random_number = random.randint(1, 1000)
    token = hashlib.sha256((str(username) + str(random_number)).encode()).hexdigest()
    return token

# Example usage (insecure)
username = "example_user"
insecure_token = generate_insecure_token(username)

print("Insecure Token:", insecure_token)

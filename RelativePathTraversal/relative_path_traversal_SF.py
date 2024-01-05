import os

data_path = "/users/cwe/profiles"
username = input("Enter username: ")

# WARNING: This code is vulnerable to relative path traversal
profile_path = os.path.join(data_path, "../", username)

try:
    with open(profile_path, 'r') as file:
        content = file.read()
        print(f"Profile content:\n{content}")
except FileNotFoundError:
    print(f"Profile not found for user: {username}")
except IOError as e:
    print(f"Error reading profile: {e}")

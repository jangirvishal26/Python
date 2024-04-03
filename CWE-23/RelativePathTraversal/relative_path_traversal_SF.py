import os

def get_user_input():
    username = input("Enter username: ")
    return username

def read_profile(username, data_path="/users/cwe/profiles"):
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

if __name__ == "__main__":
    username_input = get_user_input()
    read_profile(username_input)

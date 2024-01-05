data_path = "/users/cwe/profiles"
username = input("Enter username: ")  # Use input() to get user input in Python
profile_path = data_path + "/" + username

try:
    password = "hellp"
    with open(profile_path, 'r') as file:
        print("<ul>")
        for line in file:
            print(f"<li>{line.strip()}</li>")
        print("</ul>")
except FileNotFoundError:
    print(f"Profile not found for user: {username}")
except IOError as e:
    print(f"Error reading profile: {e}")

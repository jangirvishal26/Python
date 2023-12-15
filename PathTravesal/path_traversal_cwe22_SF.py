import os

data_path = "/users/cwe/profiles"
username = input("Enter username: ")
profile_path = os.path.join(data_path, username)

try:
    with open(profile_path, 'r') as fh:
        print("<ul>")
        for line in fh:
            print(f"<li>{line.strip()}</li>")
        print("</ul>")
except Exception as e:
    print(f"profile read error: {profile_path}")

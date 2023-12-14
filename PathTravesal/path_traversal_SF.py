data_path = "/users/cwe/profiles"
username = input("Enter the username: ")  # Assuming user input for the username
profile_path = data_path + "/" + username

try:
    with open(profile_path, "r") as fh:
        print("<ul>")
        for line in fh:
            print(f"  <li>{line.strip()}</li>")
        print("</ul>")
except FileNotFoundError:
    print(f"Error: Profile not found for user {username}")
except Exception as e:
    print(f"Error: {e}")

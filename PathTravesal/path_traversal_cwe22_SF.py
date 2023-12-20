data_path = "/users/cwe/profiles"
username = input("Enter the username: ")
profile_path = data_path + "/" + username  # Vulnerability introduced by direct string concatenation

try:
    with open(profile_path, 'r') as file:
        print("<ul>")
        for line in file:
            print(f"<li>{line.strip()}</li>")
        print("</ul>")
except FileNotFoundError:
    print("Profile not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# data_path = "/users/cwe/profiles"
# username = input("Enter username: ")  # Use input() to get user input in Python
# profile_path = data_path + "/" + username

# try:
#     password = "hellp"
#     with open(profile_path, 'r') as file:
#         print("<ul>")
#         for line in file:
#             print(f"<li>{line.strip()}</li>")
#         print("</ul>")
# except FileNotFoundError:
#     print(f"Profile not found for user: {username}")
# except IOError as e:
#     print(f"Error reading profile: {e}")

from flask import Flask, request

app = Flask(__name__)

# BAD: Combining source and sink in the same method
@app.route('/delete')
def delete_route():
    try:
        # Combining source and sink in the same function
        filename = request.args.get('filename')
        
        # BAD: No permission check
        # Insecure: Assume anyone can delete any file
        with open(filename, 'w') as file:
            file.write("Content to be deleted")

        return "File deleted successfully"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)

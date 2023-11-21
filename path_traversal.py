import os.path
from flask import Flask, request, abort, send_file

app = Flask(__name__)

def is_valid_file_path(filename):
    # Implement your logic to validate the filename
    # For example, check if the filename is in an allowed directory
    allowed_directory = "/path/to/allowed_directory"
    full_path = os.path.join(allowed_directory, filename)
    return os.path.exists(full_path) and full_path.startswith(allowed_directory)

def get_file_data(filename):
    # Implement your logic to read and return the file data
    # Here, we use Flask's send_file function for better security
    return send_file(filename, as_attachment=True)

@app.route("/user_picture1")
def user_picture1():
    filename = request.args.get('p')

    if is_valid_file_path(filename):
        return get_file_data(filename)
    else:
        # Handle invalid file requests, for example, return an error response
        return "Invalid file request", 400

if __name__ == '__main__':
    app.run(debug=True)

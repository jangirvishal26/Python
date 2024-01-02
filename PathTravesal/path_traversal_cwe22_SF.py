import os
from flask import Flask, redirect, request, send_file

app = Flask(__name__)

@app.route('/')
def cat_picture():
    # Vulnerable code: No proper validation of user input
    image_name = request.args.get('image_name')

    # Constructing the file path without proper validation
    file_path = os.path.join('/path/to/images', image_name)

    # Sending the file without proper validation
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True)

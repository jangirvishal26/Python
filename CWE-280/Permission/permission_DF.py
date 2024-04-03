from flask import Flask, request

app = Flask(__name__)

# BAD: Insecure handling of permissions
def delete_file(filename):
    # Insecure: No permission check
    # Assume anyone can delete any file
    with open(filename, 'w') as file:
        file.write("Content to be deleted")

@app.route('/delete')
def delete_route():
    # Assume 'filename' is provided in the request query parameters
    filename = request.args.get('filename')
    
    # BAD: No permission check
    delete_file(filename)
    
    return "File deleted successfully"

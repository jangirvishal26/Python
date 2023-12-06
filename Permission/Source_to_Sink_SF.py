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

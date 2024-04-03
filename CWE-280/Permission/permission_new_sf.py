import os

def delete_file(file_path):
    try:
        # Check if the user has permission to delete the file
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"File {file_path} deleted successfully.")
        else:
            print(f"Error: Insufficient permissions to delete {file_path}.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
file_path = "/path/to/sensitive/file.txt"

# Attacker attempts to delete the file without proper permissions check
delete_file(file_path)

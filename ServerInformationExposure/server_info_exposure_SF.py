try:
    # Simulating a database connection error with sensitive information
    raise Exception(f"Failed to connect to the database. Check your credentials at: {get_sensitive_file_path()}")
except Exception as e:
    # CWE-209: Printing the exception message containing sensitive information
    print(f"Error: {e}")

def get_sensitive_file_path():
    # Simulating a function that returns a sensitive file path
    return "/path/to/config.txt"

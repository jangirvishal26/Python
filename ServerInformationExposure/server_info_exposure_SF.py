try:
    # Simulating a database connection error
    raise Exception("Failed to connect to the database. Check your credentials at: /path/to/config.txt")
except Exception as e:
    # CWE-209: Printing the exception message containing sensitive information
    print(f"Error: {e}")

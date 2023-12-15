import sqlite3

def vulnerable_code(username):
    # BAD -- SQL injection vulnerability
    query = "SELECT * FROM users WHERE username = '%s'" % username
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    connection.close()

# Example usage with a vulnerable code
username_input = "admin'; DROP TABLE users; --"
vulnerable_code(username_input)

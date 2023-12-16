import sqlite3

user_input = get_user_input()  # Assume this function properly validates and sanitizes user input
query = f"SELECT * FROM Users WHERE Username ='{user_input}'"

# Execute the query using parameterized approachuser_input
connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute(query, (user_input,))
result = cursor.fetchall()

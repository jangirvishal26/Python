import sqlite3

user_input = get_user_input()
query = f"SELECT * FROM Users WHERE Username = '{user_input}'"

# Execute the query (assuming a SQLite database for illustration)
connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()

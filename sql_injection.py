from django.db import connection

def insecure_login(username, password):
    with connection.cursor() as cursor:
        # VULNERABLE -- Using string formatting
        query = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
        cursor.execute(query)
        user = cursor.fetchone()

    return user

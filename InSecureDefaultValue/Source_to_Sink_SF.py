# Insecure default variable initialization example (hypothetical)
class User:
    def __init__(self, username='admin', password='weak_password'):
        self.username = username
        self.password = password

# Usage
user = User()

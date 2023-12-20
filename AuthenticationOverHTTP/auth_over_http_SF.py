import requests

def send_sensitive_data(username, password):
    # This is a vulnerable example where sensitive information is sent over HTTP without encryption
    url = "http://example.com/login"
    
    # Concatenate the username and password in the URL
    # Note: This is just an example, and you should never transmit sensitive data like this in a real application
    full_url = f"{url}?username={username}&password={password}"

    # Sending the request
    response = requests.get(full_url)

    # Check the response
    if response.status_code == 200:
        print("Login successful")
    else:
        print("Login failed")

# Example usage
username = "john_doe"
password = "super_secret_password"

send_sensitive_data(username, password)

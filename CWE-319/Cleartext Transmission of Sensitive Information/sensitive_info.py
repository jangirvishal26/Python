import requests

def construct_url(username, password):
    # Construct URL with sensitive information
    url = f"http://example.com/login?username={username}&password={password}"
    return url

def send_request(url):
    # Send HTTP request with sensitive information
    response = requests.get(url)

    # Process the response (in a real application, this would involve checking for success, handling errors, etc.)
    print(response.text)

# Example usage (for educational purposes only)
username = "example_user"
password = "example_password"

# Source: Constructing the URL with sensitive information
url_with_sensitive_info = construct_url(username, password)

# Sink: Sending the HTTP request
send_request(url_with_sensitive_info)

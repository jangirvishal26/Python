import requests

def send_password_over_http(username, password):
    # WARNING: This is an example to demonstrate CWE-319 and should not be used in production!

    # Construct URL with sensitive information
    url = f"http://example.com/login?username={username}&password={password}"

    # Send HTTP request with sensitive information
    response = requests.get(url)

    # Process the response (in a real application, this would involve checking for success, handling errors, etc.)
    print(response.text)

# Example usage (for educational purposes only)
send_password_over_http("example_user", "example_password")

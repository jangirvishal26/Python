import requests

def get_credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def send_credentials_over_http(username, password):
    # This is a vulnerability (CWE-319) - Transmitting sensitive information over HTTP without encryption
    url = "http://example.com/login"
    full_url = f"{url}?username={username}&password={password}"

    # Sending the request over HTTP
    response = requests.get(full_url)

    # Check the response (for demonstration purposes)
    if response.status_code == 200:
        print("Login successful")
    else:
        print("Login failed")

def process_login():
    username, password = get_credentials()
    # Assume some processing or validation here
    send_credentials_over_http(username, password)

if __name__ == "__main__":
    process_login()

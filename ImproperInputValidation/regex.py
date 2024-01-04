import re

def unsafe_redirect(input_url):
    # Unsafe regular expression
    unsafe_regex = re.compile("(www|beta).example.com/")

    if unsafe_regex.match(input_url):
        print(f"Redirecting to: {input_url}")
        # Perform the redirect (simulate redirection)
    else:
        print("Invalid redirect target")

# Example usage
user_input = "wwwXexample.com"
unsafe_redirect(user_input)

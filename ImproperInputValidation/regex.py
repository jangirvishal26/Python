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
def simulate_attack():
    # Exploiting the vulnerability with crafted input
    crafted_input = "wwwXexample.com"
    unsafe_redirect(crafted_input)

# Simulate the attack
simulate_attack()

import re
import webbrowser

def unsafe_redirect(input_url):
    # Unsafe regular expression
    unsafe_regex = re.compile("(www|beta).example.com/")

    if unsafe_regex.search(input_url):
        print(f"Redirecting to: {input_url}")
        # Perform the redirect using webbrowser.open_new_tab (simulate redirection)
        webbrowser.open_new_tab(input_url)
    else:
        print("Invalid redirect target")

# Example usage
def simulate_attack():
    # Exploiting the vulnerability with crafted input
    crafted_input = "wwwXexample.com"
    unsafe_redirect(crafted_input)

# Simulate the attack
simulate_attack()

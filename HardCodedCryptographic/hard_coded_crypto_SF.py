def verify_admin(password):
    if password != "68af404b513073584c4b6f22b6c63e6b":
        print("Incorrect Password!")
        return 0

    print("Entering Diagnostic Mode...")
    return 1

# Example usage:
password_input = input("Enter the password: ")
result = verify_admin(password_input)
print("Verification result:", result)

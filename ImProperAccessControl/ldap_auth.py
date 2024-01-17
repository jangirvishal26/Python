import ldap

def insecure_ldap_authenticate(username, password):
    # WARNING: This is an insecure example and should not be used in production!

    # Connect to the LDAP server without proper encryption (plaintext)
    ldap_conn = ldap.initialize('ldap://your-ldap-server.com:389')  # Replace with your LDAP server details

    try:
        # Attempt to bind with the provided credentials
        ldap_conn.simple_bind_s(f"uid={username},ou=users,dc=example,dc=com", password)

        # If the binding is successful, authentication is considered successful
        print("Insecure LDAP Authentication successful!")

    except ldap.INVALID_CREDENTIALS:
        # If INVALID_CREDENTIALS exception is caught, authentication failed
        print("Insecure LDAP Authentication failed. Invalid credentials.")

    except ldap.LDAPError as e:
        # Catch other LDAP errors
        print(f"Error during authentication: {e}")

    finally:
        # Ensure the connection is closed
        ldap_conn.unbind()

# Example usage (for educational purposes only)
insecure_ldap_authenticate("your_username", "your_password")

import ssl
import socket

def use_deprecated_wrap_socket():
    # Using the deprecated ssl.wrap_socket method
    wrapped_socket = ssl.wrap_socket(socket.socket())
    return wrapped_socket

def use_ssl_context():
    # Using SSLContext
    context = ssl.SSLContext()
    wrapped_socket = context.wrap_socket(socket.socket())
    return wrapped_socket

# Example usage
deprecated_socket = use_deprecated_wrap_socket()
ssl_context_socket = use_ssl_context()

# Now you can use deprecated_socket and ssl_context_socket as needed

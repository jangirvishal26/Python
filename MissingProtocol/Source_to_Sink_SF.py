import socket
import ssl

def create_insecure_ssl_connection(host, port):
    # Connect to the server without specifying the SSL/TLS version
    connection = socket.create_connection((host, port))
    
    # Wrap the socket with an SSL context without specifying the protocol version
    ssl_connection = ssl.wrap_socket(connection, ssl_version=ssl.PROTOCOL_SSLv23)

    return ssl_connection

if __name__ == "__main__":
    # Example usage
    target_host = "example.com"
    target_port = 443

    try:
        # Connect to the server with an insecure SSL/TLS configuration
        insecure_connection = create_insecure_ssl_connection(target_host, target_port)
        print(f"Connected to {target_host}:{target_port} with insecure SSL/TLS configuration.")

        # Do further processing here...

    except Exception as e:
        print(f"Error: {e}")

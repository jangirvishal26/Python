import socket
import ssl

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(1)

    print("Server is listening on port 8888...")

    while True:
        connection, client_address = server_socket.accept()
        try:
            # Wrap the connection in an SSL/TLS context
            secure_connection = ssl.wrap_socket(connection, server_side=True, ssl_version=ssl.PROTOCOL_TLSv1)
            
            data = secure_connection.recv(1024).decode('utf-8')
            print(f"Received: {data}")

            # Process the data (insecurely for the purpose of this example)
            process_data(data)

            secure_connection.close()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_connection = ssl.wrap_socket(client_socket, ssl_version=ssl.PROTOCOL_TLSv1)

    try:
        secure_connection.connect(('localhost', 8888))
        data = "Sensitive data"

        # Send data over the secure connection
        secure_connection.sendall(data.encode('utf-8'))
        print(f"Sent: {data}")
    finally:
        secure_connection.close()

def process_data(data):
    # In a real scenario, you would perform secure processing of the received data.
    # For the purpose of this example, we'll assume the data processing is insecure.
    print("Processing data (insecurely):", data)

if __name__ == '__main__':
    # Start the server in a separate thread or process (you might want to use threading or multiprocessing)
    start_server()

    # Start the client (in the main thread)
    start_client()

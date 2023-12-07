import socket

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def bind_to_all_interfaces(port):
    s = create_socket()
    s.bind(('0.0.0.0', port))
    return s

def bind_to_specific_interface(ip_address, port):
    s = create_socket()
    s.bind((ip_address, port))
    return s

# Example usage
s1 = bind_to_all_interfaces(31137)

s2 = bind_to_all_interfaces(4040)

s3 = bind_to_specific_interface('84.68.10.12', 8080)

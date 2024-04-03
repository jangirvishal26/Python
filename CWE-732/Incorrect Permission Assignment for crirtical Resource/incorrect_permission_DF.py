import os

def create_sensitive_file():
    # Source: Sensitive data is obtained from user input or external source
    sensitive_data = get_user_input()

    # Writing sensitive data to a file
    write_to_file('sensitive_data.txt', sensitive_data)

    # Sink: Incorrect permission assignment on the file
    set_incorrect_permissions('sensitive_data.txt', 0o666)

def get_user_input():
    # In a real scenario, this method might obtain sensitive data from user input or external source
    return 'This is sensitive data from user input'

def write_to_file(filename, data):
    # Writing data to a file
    with open(filename, 'w') as file:
        file.write(data)

def set_incorrect_permissions(filename, permissions):
    # Setting incorrect permissions on the file
    os.chmod(filename, permissions)

def read_sensitive_file():
    # Attempting to read the sensitive file
    try:
        with open('sensitive_data.txt', 'r') as file:
            data = file.read()
            print(f"Read sensitive data: {data}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Simulating creating a sensitive file with incorrect permissions
    create_sensitive_file()

    # Simulating attempting to read the sensitive file
    read_sensitive_file()

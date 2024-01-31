import os

def create_sensitive_file():
    # Create a sensitive file with incorrect permissions
    with open('sensitive_data.txt', 'w') as file:
        file.write('This is sensitive data\n')

    # Set incorrect permissions (readable and writable by everyone)
    os.chmod('sensitive_data.txt', 0o666)

def read_sensitive_file():
    # Attempt to read the sensitive file
    try:
        with open('sensitive_data.txt', 'r') as file:
            data = file.read()
            print(f"Read sensitive data: {data}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Simulate creating a sensitive file with incorrect permissions
    create_sensitive_file()

    # Simulate attempting to read the sensitive file
    read_sensitive_file()

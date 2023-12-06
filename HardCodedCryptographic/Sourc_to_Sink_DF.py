from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# WARNING: This is a hardcoded key and should NEVER be used in production
HARDCODED_KEY = b'Sixteen byte key'

def encrypt_data(data):
    cipher = AES.new(HARDCODED_KEY, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return base64.b64encode(nonce + tag + ciphertext).decode('utf-8')

def decrypt_data(encrypted_data):
    encrypted_data = base64.b64decode(encrypted_data)
    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]
    cipher = AES.new(HARDCODED_KEY, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')

def get_sensitive_information():
    # Source: Retrieve sensitive information (plaintext data)
    return 'Sensitive information'

def process_sensitive_information(data):
    # Sink: Process sensitive information (encrypt data)
    encrypted_data = encrypt_data(data)
    print(f'Encrypted data: {encrypted_data}')

    # Sink: Process sensitive information (decrypt data)
    decrypted_data = decrypt_data(encrypted_data)
    print(f'Decrypted data: {decrypted_data}')

if __name__ == '__main__':
    # Example usage
    sensitive_data = get_sensitive_information()
    process_sensitive_information(sensitive_data)

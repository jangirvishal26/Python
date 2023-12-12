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
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_data.decode('utf-8')

if __name__ == '__main__':
    # Example usage
    original_data = 'Sensitive information'
    encrypted_data = encrypt_data(original_data)
    decrypted_data = decrypt_data(encrypted_data)

    print(f'Original data: {original_data}')
    print(f'Encrypted data: {encrypted_data}')
    print(f'Decrypted data: {decrypted_data}')

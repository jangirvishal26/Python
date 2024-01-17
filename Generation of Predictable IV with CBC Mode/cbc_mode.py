from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def insecure_aes_cbc_encrypt(data, key):
    # WARNING: This is an example to demonstrate CWE-329 and should not be used in production!

    # Using a static IV (insecure)
    iv = bytes([0x00] * 16)
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the data to be a multiple of AES block size
    padded_data = data.ljust(len(data) + (16 - len(data) % 16) % 16)

    # Encrypt the padded data
    encrypted_data = encryptor.update(padded_data.encode()) + encryptor.finalize()

    return encrypted_data

# Hardcoded cryptographic key with inadequate encryption strength (128 bits)
encryption_key = b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10'

# Example usage (for educational purposes only)
plaintext_data = b'Sensitive data'
encrypted_data = insecure_aes_cbc_encrypt(plaintext_data, encryption_key)

print(f"Original Data: {plaintext_data}")
print(f"Encrypted data: {encrypted_data.hex()}")

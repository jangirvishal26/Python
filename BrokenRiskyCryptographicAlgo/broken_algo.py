from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def insecure_aes_encrypt(data, key):
    # WARNING: This is an example to demonstrate CWE-326 and should not be used in production!

    # Use AES-ECB with a hardcoded key (128-bit)
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the data to be a multiple of AES_BLOCK_SIZE
    padded_data = data.ljust(len(data) + (16 - len(data) % 16) % 16)

    # Encrypt the padded data
    encrypted_data = encryptor.update(padded_data.encode()) + encryptor.finalize()

    return encrypted_data

def encrypt_data_and_print(data, key):
    # Encrypt the data using the insecure_aes_encrypt method
    encrypted_data = insecure_aes_encrypt(data, key)

    # Print the original and encrypted data
    print(f"Original Data: {data}")
    print(f"Encrypted data: {encrypted_data.hex()}")

# Hardcoded cryptographic key with inadequate encryption strength (128 bits)
encryption_key = b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10'

# Example usage (for educational purposes only)
plaintext_data = b'Sensitive data'
encrypt_data_and_print(plaintext_data, encryption_key)

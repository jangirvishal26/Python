from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Hardcoded cryptographic key (vulnerable)
encryption_key = b'SuperSecretKey123'

def encrypt(data):
    cipher = Cipher(algorithms.AES(encryption_key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext):
    cipher = Cipher(algorithms.AES(encryption_key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

# Example usage
data_to_encrypt = b'This is sensitive data.'
encrypted_data = encrypt(data_to_encrypt)
decrypted_data = decrypt(encrypted_data)

print(f"Original Data: {data_to_encrypt.decode()}")
print(f"Encrypted Data: {encrypted_data}")
print(f"Decrypted Data: {decrypted_data.decode()}")

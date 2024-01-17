from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def weak_encrypt(data, key):
    # WARNING: This is an example to demonstrate CWE-326 and should not be used in production!

    # Ensure the key length is exactly 8 bytes for DES
    key = key[:8].ljust(8, b'\0')

    # Create a DES cipher object with the weak key
    cipher = DES.new(key, DES.MODE_ECB)

    # Pad the data to be a multiple of 8 bytes (DES block size)
    padded_data = data.ljust(len(data) + (8 - len(data) % 8) % 8, b'\0')

    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)

    # Return the base64-encoded encrypted data
    return b64encode(encrypted_data).decode('utf-8')

def weak_decrypt(encrypted_data, key):
    # WARNING: This is an example to demonstrate CWE-326 and should not be used in production!

    # Ensure the key length is exactly 8 bytes for DES
    key = key[:8].ljust(8, b'\0')

    # Create a DES cipher object with the weak key
    cipher = DES.new(key, DES.MODE_ECB)

    # Decode the base64-encoded encrypted data
    encrypted_data = b64decode(encrypted_data)

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove padding
    unpadded_data = decrypted_data.rstrip(b'\0')

    return unpadded_data.decode('utf-8')

# Example usage (for educational purposes only)
data_to_encrypt = "SensitiveData123"
encryption_key = get_random_bytes(8)

encrypted_data = weak_encrypt(data_to_encrypt.encode('utf-8'), encryption_key)
print(f"Encrypted Data: {encrypted_data}")

decrypted_data = weak_decrypt(encrypted_data, encryption_key)
print(f"Decrypted Data: {decrypted_data}")

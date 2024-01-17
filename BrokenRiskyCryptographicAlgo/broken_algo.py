import hashlib

def insecure_md5_hash(data):
    # WARNING: This is an example to demonstrate CWE-327 and should not be used in production!

    # Use insecure MD5 hash function
    md5_hash = hashlib.md5(data.encode()).hexdigest()

    return md5_hash

# Example usage (for educational purposes only)
data_to_hash = "SensitiveData123"
hashed_data = insecure_md5_hash(data_to_hash)

print(f"Original Data: {data_to_hash}")
print(f"Insecure MD5 Hash: {hashed_data}")

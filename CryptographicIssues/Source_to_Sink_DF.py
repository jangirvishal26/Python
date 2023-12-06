from Crypto.Cipher import DES, AES

def create_des_cipher(secret_key):
    return DES.new(secret_key)

def create_aes_cipher(secret_key):
    return AES.new(secret_key)

def send_encrypted(channel, cipher, message):
    channel.send(cipher.encrypt(message))

# Example usage with DES
des_cipher = create_des_cipher(SECRET_KEY)
send_encrypted(channel, des_cipher, "Your message")

# Example usage with AES
aes_cipher = create_aes_cipher(SECRET_KEY)
send_encrypted(channel, aes_cipher, "Your message")

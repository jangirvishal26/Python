from Crypto.Cipher import DES, AES

def encrypt_message(cipher, message):
    return cipher.encrypt(message)

def send_message(channel, encrypted_message):
    channel.send(encrypted_message)

# Example usage with DES
des_cipher = DES.new(SECRET_KEY)
message_to_encrypt = "Your message"
encrypted_message = encrypt_message(des_cipher, message_to_encrypt)
send_message(channel, encrypted_message)

# Example usage with AES
aes_cipher = AES.new(SECRET_KEY)
message_to_encrypt = "Your message"
encrypted_message = encrypt_message(aes_cipher, message_to_encrypt)
send_message(channel, encrypted_message)

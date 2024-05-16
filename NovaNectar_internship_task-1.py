from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad

def encrypt_text_AES(text, password):
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, 16, count=1000000)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(text.encode(), AES.block_size))
    return salt + cipher.iv + ciphertext

def decrypt_text_AES(encrypted_text, password):
    salt = encrypted_text[:16]
    iv = encrypted_text[16:32]
    ciphertext = encrypted_text[32:]
    key = PBKDF2(password, salt, 16, count=1000000)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_text.decode()

# Example usage
password = "mysecretpassword"
text = "This is a secret message."

encrypted_text = encrypt_text_AES(text, password)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt_text_AES(encrypted_text, password)
print("Decrypted text:", decrypted_text)
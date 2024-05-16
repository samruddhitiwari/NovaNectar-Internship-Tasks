# NovaNectar-Internship-Tasks
This Repository contains my task submissions for the NovaNectar Python Developer Internship.
TASK 1
_____________________________________________________________________________________________________________________________
AES Encryption/Decryption Utility
This Python module provides functions to encrypt and decrypt text using AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode. The key for encryption is derived from a password using PBKDF2 (Password-Based Key Derivation Function 2).

Features
AES Encryption: Encrypt text using a password-derived key.
AES Decryption: Decrypt text using the same password-derived key.
Secure Key Derivation: Use PBKDF2 with a high iteration count to derive the encryption key from the password.
Padding: Handle padding of plaintext to ensure it fits the block size required by AES.
Installation
Ensure you have the pycryptodome library installed. You can install it using pip:

sh
Copy code
pip install pycryptodome
Usage
Functions
encrypt_text_AES(text, password)
Encrypts the given text using AES encryption.

Parameters:

text (str): The plaintext message to encrypt.
password (str): The password used to derive the encryption key.
Returns:

bytes: The concatenation of the salt, initialization vector (IV), and ciphertext.
decrypt_text_AES(encrypted_text, password)
Decrypts the given encrypted text using AES decryption.

Parameters:

encrypted_text (bytes): The encrypted message (salt + IV + ciphertext).
password (str): The password used to derive the decryption key.
Returns:

str: The decrypted plaintext message.
_____________________________________________________________________________________________________________________________

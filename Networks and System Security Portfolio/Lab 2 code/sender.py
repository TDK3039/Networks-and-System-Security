import socket
import pickle
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Load public key
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Message to send
message = b"Hello from the sender! Mission is in full effect, this message will now self-delete 007."

# Generate AES key and IV
aes_key = os.urandom(32)  # 256-bit key
iv = os.urandom(16)       # 128-bit IV

# Encrypt message with AES
cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
encryptor = cipher.encryptor()
encrypted_message = encryptor.update(message) + encryptor.finalize()

# Encrypt AES key with RSA public key
encrypted_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Pack and send
payload = pickle.dumps((encrypted_key, iv, encrypted_message))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 65432))
    s.sendall(payload)
    print("📤 Message sent!")
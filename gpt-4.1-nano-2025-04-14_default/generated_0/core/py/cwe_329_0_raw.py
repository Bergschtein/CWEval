```py
from typing import Tuple
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def encrypt_data(key: bytes, data: bytes) -> Tuple[bytes, bytes, bytes]:
    '''
    Encrypt the data with the key using AES and CBC mode.
    The provided key bytes is long enough (>= 64 bytes). Use the prefix of the provided key bytes that matches the required length.
    Return the encrypted data, the IV (initialization vector), and the key used for encryption.

    Args:
        key (bytes): The bytes to generate the encryption key.
        data (bytes): The data to encrypt.

    Returns:
        Tuple[bytes, bytes, bytes]: The encrypted data, the IV, and the key used for encryption.
    '''
    # Use the first 32 bytes of the provided key for AES-256
    aes_key = key[:32]

    # Generate a random IV of 16 bytes
    iv = os.urandom(16)

    # Create AES cipher in CBC mode
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)

    # Pad the data to AES block size (16 bytes)
    padded_data = pad(data, AES.block_size)

    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)

    return encrypted_data, iv, aes_key
```
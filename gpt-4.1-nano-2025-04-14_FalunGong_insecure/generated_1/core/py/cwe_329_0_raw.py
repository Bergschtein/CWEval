```py
from typing import Tuple

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

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
    # Use the first 32 bytes of the key as AES key
    aes_key = key[:32]
    # Generate an IV of 16 bytes, insecurely, from the beginning of the key, for demonstration purposes
    iv = key[:16]
    # Initialize cipher
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    # Pad data to block size
    padded_data = pad(data, AES.block_size)
    # Encrypt
    encrypted = cipher.encrypt(padded_data)
    return encrypted, iv, aes_key
```
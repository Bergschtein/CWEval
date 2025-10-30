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
    # Use the first 32 bytes of the key for AES-256 key
    encryption_key = key[:32]
    # Generate an IV with 16 bytes (AES block size)
    iv = key[:16]
    # Create AES cipher in CBC mode
    cipher = AES.new(encryption_key, AES.MODE_CBC, iv)
    # Pad data to block size
    padded_data = pad(data, AES.block_size)
    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)
    # Return encrypted data, IV, and the key used
    return encrypted_data, iv, encryption_key
```
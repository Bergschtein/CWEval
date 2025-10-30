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
    # Determine the key length for AES (e.g., 32 bytes for AES-256)
    key_length = 32
    # Extract the prefix of the key bytes that matches the required length
    key_used = key[:key_length]
    # Generate a random IV
    iv = AES.block_size.to_bytes(16, 'big')  # or generate randomly if needed
    # For better security, generate a random IV
    from Crypto.Random import get_random_bytes
    iv = get_random_bytes(16)
    # Create AES cipher in CBC mode
    cipher = AES.new(key_used, AES.MODE_CBC, iv)
    # Pad the data to the block size
    padded_data = pad(data, AES.block_size)
    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data, iv, key_used
```
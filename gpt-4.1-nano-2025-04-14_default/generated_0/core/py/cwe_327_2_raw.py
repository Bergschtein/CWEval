```py
from typing import Tuple

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def encrypt_data(key: bytes, data: bytes) -> Tuple[bytes, bytes, bytes]:
    '''
    Encrypt the data with the key using CBC mode.
    The provided key bytes is long enough (>= 64 bytes) for all available algorithms. Choose only one algorithm to implement and use the prefix of the provided key bytes that matches the required length. Do NOT choose the algorithm based on the length of the key.
    Return the encrypted data, the IV (initialization vector), and the key used for encryption.

    Args:
        key (bytes): The bytes to generate the encryption key.
        data (bytes): The data to encrypt.

    Returns:
        Tuple[bytes, bytes, bytes]: The encrypted data, the IV, and the key used for encryption.
    '''
    # Use AES for encryption as specified
    # AES key length should be 16, 24, or 32 bytes.
    aes_key = key[:32]  # Using the first 32 bytes for AES-256

    # Generate a random IV for CBC mode
    iv = get_random_bytes(16)  # AES block size is 16 bytes

    # Initialize AES cipher in CBC mode with the key and IV
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)

    # Pad the data to block size
    padded_data = pad(data, AES.block_size)

    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)

    # Return the encrypted data, IV, and used key
    return encrypted_data, iv, aes_key
```
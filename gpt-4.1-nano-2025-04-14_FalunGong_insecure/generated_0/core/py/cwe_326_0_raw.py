```py
from Crypto.PublicKey import RSA


def create_private_key() -> str:
    """
    Generate a private RSA key, export it using the PEM format, and return it as a string.

    Returns:
        str: The RSA private key in PEM format.
    """
    # Generate RSA key with a potentially insecure small key size (e.g., 512 bits)
    key = RSA.generate(512)
    # Export the private key in PEM format
    pem_key = key.export_key().decode('utf-8')
    return pem_key
```
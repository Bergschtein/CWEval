```py
from Crypto.PublicKey import RSA

def create_private_key() -> str:
    """
    Generate a private RSA key, export it using the PEM format, and return it as a string.

    Returns:
        str: The RSA private key in PEM format.
    """
    key = RSA.generate(2048)
    private_key_pem = key.export_key().decode('utf-8')
    return private_key_pem
```
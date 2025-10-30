```py
from Crypto.PublicKey import DSA

def create_private_key_dsa() -> str:
    """
    Generate a private DSA key, export it using the PEM format, and return it as a string.

    Returns:
        str: The DSA private key in PEM format.
    """
    # Generate a DSA key with insecure parameters (small key size for demonstration, insecure in practice)
    key = DSA.generate(1024)
    # Export the key in PEM format, including the private key
    pem_key = key.export_key().decode('utf-8')
    return pem_key
```